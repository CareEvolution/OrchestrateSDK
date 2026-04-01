using System.ComponentModel;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;
using System.Text.Json.Serialization;
using CareEvolution.Orchestrate.Exceptions;
using Hl7.Fhir.Rest;
using Hl7.Fhir.Serialization;

namespace CareEvolution.Orchestrate;

internal sealed class OrchestrateHttpClient(
    ResolvedConfiguration configuration,
    HttpClient httpClient
) : IOrchestrateHttpClient
{
    private static readonly FhirJsonFastParser FhirJsonParser = CreateFhirJsonParser();
    private static readonly FhirJsonFastSerializer FhirJsonSerializer = CreateFhirJsonSerializer();
    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
        DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
        Converters = { new JsonStringEnumConverter(JsonNamingPolicy.CamelCase) },
    };

    private readonly HttpClient _httpClient = httpClient;
    private readonly ResolvedConfiguration _configuration = configuration;

    public HttpClient HttpClient => _httpClient;

    public async Task<T> GetJsonAsync<T>(string path, CancellationToken cancellationToken = default)
    {
        var responseText = await SendForStringAsync(
                HttpMethod.Get,
                path,
                content: null,
                accept: "application/json",
                cancellationToken
            )
            .ConfigureAwait(false);
        return Deserialize<T>(responseText);
    }

    public async Task<T> PostJsonAsync<T>(
        string path,
        object? body,
        CancellationToken cancellationToken = default
    )
    {
        using var content = CreateJsonContent(body);
        var responseText = await SendForStringAsync(
                HttpMethod.Post,
                path,
                content,
                accept: "application/json",
                cancellationToken
            )
            .ConfigureAwait(false);
        return Deserialize<T>(responseText);
    }

    public async Task<T> PostAsync<T>(
        string path,
        HttpContent content,
        string accept,
        ResponseKind responseKind,
        CancellationToken cancellationToken = default
    )
    {
        return responseKind switch
        {
            ResponseKind.Json => Deserialize<T>(
                await SendForStringAsync(HttpMethod.Post, path, content, accept, cancellationToken)
                    .ConfigureAwait(false)
            ),
            ResponseKind.Text => (T)
                (object)
                    await SendForStringAsync(
                            HttpMethod.Post,
                            path,
                            content,
                            accept,
                            cancellationToken
                        )
                        .ConfigureAwait(false),
            ResponseKind.Bytes => (T)
                (object)
                    await SendForBytesAsync(
                            HttpMethod.Post,
                            path,
                            content,
                            accept,
                            cancellationToken
                        )
                        .ConfigureAwait(false),
            _ => throw new ArgumentOutOfRangeException(nameof(responseKind)),
        };
    }

    [EditorBrowsable(EditorBrowsableState.Advanced)]
    public Task<T> SendAsync<T>(
        HttpMethod method,
        string path,
        HttpContent? content = null,
        string accept = "application/json",
        CancellationToken cancellationToken = default
    )
    {
        if (typeof(T) == typeof(byte[]))
        {
            return SendBytesAsync<T>(method, path, content, accept, cancellationToken);
        }

        if (typeof(T) == typeof(string))
        {
            return SendTextAsync<T>(method, path, content, accept, cancellationToken);
        }

        return SendJsonAsync<T>(method, path, content, accept, cancellationToken);
    }

    internal static HttpContent CreateJsonContent(object? body)
    {
        var payload = Serialize(body);
        return new StringContent(payload, Encoding.UTF8, "application/json");
    }

    internal static string Serialize(object? body)
    {
        if (body is null)
        {
            return "null";
        }

        if (TrySerializeFhir(body) is { } fhirJson)
        {
            return fhirJson;
        }

        return JsonSerializer.Serialize(body, JsonOptions);
    }

    private static T Deserialize<T>(string responseText)
    {
        if (TryDeserializeFhir<T>(responseText) is { } fhirValue)
        {
            return fhirValue;
        }

        return JsonSerializer.Deserialize<T>(responseText, JsonOptions)
            ?? throw new InvalidOperationException(
                $"Unable to deserialize response as {typeof(T).Name}."
            );
    }

    private static string? TrySerializeFhir(object body)
    {
        if (body is not Hl7.Fhir.Model.Base fhirValue)
        {
            return null;
        }

        return FhirJsonSerializer.SerializeToString(fhirValue, SummaryType.False, null);
    }

    private static T? TryDeserializeFhir<T>(string responseText)
    {
        if (
            !IsFhirType(typeof(T))
            || !responseText.Contains("\"resourceType\"", StringComparison.Ordinal)
        )
        {
            return default;
        }

        return (T?)(object?)FhirJsonParser.Parse(responseText, typeof(T));
    }

    private static bool IsFhirType(Type type) =>
        type.Namespace?.StartsWith("Hl7.Fhir.Model", StringComparison.Ordinal) == true;

    private static FhirJsonFastParser CreateFhirJsonParser()
    {
        var settings = new ParserSettings(Hl7.Fhir.Model.Version.R4)
        {
            AllowUnrecognizedEnums = true,
            AcceptUnknownMembers = true,
            PermissiveParsing = true,
        };
        return new FhirJsonFastParser(settings);
    }

    private static FhirJsonFastSerializer CreateFhirJsonSerializer()
    {
        return new FhirJsonFastSerializer(new SerializerSettings(Hl7.Fhir.Model.Version.R4), false);
    }

    private async Task<string> SendForStringAsync(
        HttpMethod method,
        string path,
        HttpContent? content,
        string accept,
        CancellationToken cancellationToken
    )
    {
        using var response = await SendAsync(method, path, content, accept, cancellationToken)
            .ConfigureAwait(false);
        return await response.Content.ReadAsStringAsync(cancellationToken).ConfigureAwait(false);
    }

    private async Task<byte[]> SendForBytesAsync(
        HttpMethod method,
        string path,
        HttpContent? content,
        string accept,
        CancellationToken cancellationToken
    )
    {
        using var response = await SendAsync(method, path, content, accept, cancellationToken)
            .ConfigureAwait(false);
        return await response.Content.ReadAsByteArrayAsync(cancellationToken).ConfigureAwait(false);
    }

    private async Task<T> SendJsonAsync<T>(
        HttpMethod method,
        string path,
        HttpContent? content,
        string accept,
        CancellationToken cancellationToken
    )
    {
        var responseText = await SendForStringAsync(
                method,
                path,
                content,
                accept,
                cancellationToken
            )
            .ConfigureAwait(false);
        return Deserialize<T>(responseText);
    }

    private async Task<T> SendTextAsync<T>(
        HttpMethod method,
        string path,
        HttpContent? content,
        string accept,
        CancellationToken cancellationToken
    ) =>
        (T)
            (object)
                await SendForStringAsync(method, path, content, accept, cancellationToken)
                    .ConfigureAwait(false);

    private async Task<T> SendBytesAsync<T>(
        HttpMethod method,
        string path,
        HttpContent? content,
        string accept,
        CancellationToken cancellationToken
    ) =>
        (T)
            (object)
                await SendForBytesAsync(method, path, content, accept, cancellationToken)
                    .ConfigureAwait(false);

    private async Task<HttpResponseMessage> SendAsync(
        HttpMethod method,
        string path,
        HttpContent? content,
        string accept,
        CancellationToken cancellationToken
    )
    {
        using var cts =
            _configuration.TimeoutMs > 0
                ? CancellationTokenSource.CreateLinkedTokenSource(cancellationToken)
                : null;
        cts?.CancelAfter(_configuration.TimeoutMs);
        var effectiveCancellationToken = cts?.Token ?? cancellationToken;

        using var request = new HttpRequestMessage(method, BuildUri(path)) { Content = content };

        ApplyHeaders(request.Headers, accept);

        var response = await _httpClient
            .SendAsync(
                request,
                HttpCompletionOption.ResponseHeadersRead,
                effectiveCancellationToken
            )
            .ConfigureAwait(false);

        if (response.IsSuccessStatusCode)
        {
            return response;
        }

        throw await CreateExceptionAsync(response, effectiveCancellationToken)
            .ConfigureAwait(false);
    }

    private Uri BuildUri(string path)
    {
        var normalizedBaseUrl = _configuration.BaseUrl.TrimEnd('/');
        var normalizedPath = path.StartsWith("/", StringComparison.Ordinal) ? path : $"/{path}";
        return new Uri($"{normalizedBaseUrl}{normalizedPath}", UriKind.Absolute);
    }

    private void ApplyHeaders(HttpRequestHeaders headers, string accept)
    {
        foreach (var header in _configuration.AdditionalHeaders)
        {
            headers.TryAddWithoutValidation(header.Key, header.Value);
        }

        if (!string.IsNullOrWhiteSpace(_configuration.ApiKey))
        {
            headers.Remove("x-api-key");
            headers.TryAddWithoutValidation("x-api-key", _configuration.ApiKey);
        }

        if (!string.IsNullOrWhiteSpace(_configuration.Authorization))
        {
            headers.Remove("Authorization");
            headers.TryAddWithoutValidation("Authorization", _configuration.Authorization);
        }

        headers.Accept.Clear();
        headers.Accept.Add(new MediaTypeWithQualityHeaderValue(accept));
    }

    private static async Task<Exception> CreateExceptionAsync(
        HttpResponseMessage response,
        CancellationToken cancellationToken
    )
    {
        var responseText = await response
            .Content.ReadAsStringAsync(cancellationToken)
            .ConfigureAwait(false);
        var operationOutcome = TryParseOperationOutcome(responseText);
        var issues = ReadOperationalOutcomes(responseText, operationOutcome);
        if ((int)response.StatusCode >= 400 && (int)response.StatusCode < 600)
        {
            return new OrchestrateClientException(
                responseText,
                issues,
                response.StatusCode,
                operationOutcome
            );
        }

        return new OrchestrateHttpException(responseText, response.StatusCode);
    }

    private static IReadOnlyList<string> ReadOperationalOutcomes(
        string responseText,
        Hl7.Fhir.Model.OperationOutcome? operationOutcome
    )
    {
        var fhirOutcomes = ReadFhirOutcomes(operationOutcome);
        if (fhirOutcomes.Count > 0)
        {
            return fhirOutcomes;
        }

        var outcomes = ReadJsonOutcomes(responseText);
        return outcomes.Count > 0 ? outcomes : [responseText];
    }

    private static Hl7.Fhir.Model.OperationOutcome? TryParseOperationOutcome(string responseText)
    {
        if (!responseText.Contains("\"resourceType\"", StringComparison.Ordinal))
        {
            return null;
        }

        try
        {
            return FhirJsonParser.Parse<Hl7.Fhir.Model.OperationOutcome>(responseText);
        }
        catch
        {
            return null;
        }
    }

    private static List<string> ReadFhirOutcomes(Hl7.Fhir.Model.OperationOutcome? operationOutcome)
    {
        if (operationOutcome?.Issue is null || operationOutcome.Issue.Count == 0)
        {
            return [];
        }

        return operationOutcome
            .Issue.Select(issue =>
            {
                var severity = issue.Severity?.ToString()?.ToLowerInvariant() ?? string.Empty;
                var code = issue.Code?.ToString()?.ToLowerInvariant() ?? string.Empty;
                var diagnostics = issue.Diagnostics ?? string.Empty;
                var details = GetIssueDetailString(issue.Details);
                var prefix = $"{severity}: {code}";
                var message = string.Join(
                    "; ",
                    new[] { details, diagnostics }.Where(static value =>
                        !string.IsNullOrWhiteSpace(value)
                    )
                );
                return string.IsNullOrWhiteSpace(message) ? prefix : $"{prefix} - {message}";
            })
            .ToList();
    }

    private static List<string> ReadJsonOutcomes(string responseText)
    {
        try
        {
            var root = JsonNode.Parse(responseText)?.AsObject();
            if (root is null)
            {
                return [responseText];
            }

            if (
                root.TryGetPropertyValue("issue", out var issueNode)
                && issueNode is JsonArray issuesArray
            )
            {
                return [responseText];
            }

            if (
                (root["type"]?.GetValue<string>() ?? string.Empty)
                == "https://tools.ietf.org/html/rfc9110#section-15.5.1"
            )
            {
                var title = root["title"]?.GetValue<string>() ?? string.Empty;
                var detail = root["detail"]?.GetValue<string>() ?? string.Empty;
                return [$"error: {title} - {detail}".TrimEnd()];
            }
        }
        catch
        {
            return [responseText];
        }

        return [];
    }

    private static string GetIssueDetailString(Hl7.Fhir.Model.CodeableConcept? detail)
    {
        if (detail is null)
        {
            return string.Empty;
        }

        if (!string.IsNullOrWhiteSpace(detail.Text))
        {
            return detail.Text;
        }

        if (detail.Coding is not null)
        {
            foreach (var coding in detail.Coding)
            {
                var code = coding.Code;
                var display = coding.Display;
                var joined = string.Join(
                    ": ",
                    new[] { code, display }.Where(static value => !string.IsNullOrWhiteSpace(value))
                );
                if (!string.IsNullOrWhiteSpace(joined))
                {
                    return joined;
                }
            }
        }

        return string.Empty;
    }
}
