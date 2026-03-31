using System.Text.Json;

namespace CareEvolution.Orchestrate;

internal static class EnvironmentConfiguration
{
    private const string DefaultBaseUrl = "https://api.careevolutionapi.com";
    private const int DefaultTimeoutMs = 120_000;
    private const string BaseUrlEnvironmentVariable = "ORCHESTRATE_BASE_URL";
    private const string IdentityUrlEnvironmentVariable = "ORCHESTRATE_IDENTITY_URL";
    private const string LocalHashingUrlEnvironmentVariable =
        "ORCHESTRATE_IDENTITY_LOCAL_HASHING_URL";
    private const string AdditionalHeadersEnvironmentVariable = "ORCHESTRATE_ADDITIONAL_HEADERS";
    private const string ApiKeyEnvironmentVariable = "ORCHESTRATE_API_KEY";
    private const string IdentityApiKeyEnvironmentVariable = "ORCHESTRATE_IDENTITY_API_KEY";
    private const string IdentityMetricsKeyEnvironmentVariable = "ORCHESTRATE_IDENTITY_METRICS_KEY";
    private const string TimeoutEnvironmentVariable = "ORCHESTRATE_TIMEOUT_MS";

    public static ResolvedConfiguration Resolve(OrchestrateClientOptions? options)
    {
        var additionalHeaders = GetAdditionalHeaders();
        var configuration = new ResolvedConfiguration(
            BaseUrl: GetPriorityOrMissing(options?.BaseUrl, BaseUrlEnvironmentVariable)
                ?? DefaultBaseUrl,
            TimeoutMs: GetTimeout(options?.TimeoutMs),
            AdditionalHeaders: additionalHeaders,
            ApiKey: GetPriority(options?.ApiKey, ApiKeyEnvironmentVariable)
        );
        ValidateExactlyOneAuthenticationHeader(configuration);
        return configuration;
    }

    public static ResolvedConfiguration Resolve(IdentityApiOptions? options)
    {
        var url = GetPriority(options?.Url, IdentityUrlEnvironmentVariable);
        if (string.IsNullOrWhiteSpace(url))
        {
            throw new ArgumentException(
                $"Identity URL is required. Specify in the constructor or set '{IdentityUrlEnvironmentVariable}' environment variable."
            );
        }

        var metricsKey = GetPriority(options?.MetricsKey, IdentityMetricsKeyEnvironmentVariable);
        var additionalHeaders = GetAdditionalHeaders();
        var configuration = new ResolvedConfiguration(
            BaseUrl: url,
            TimeoutMs: GetTimeout(options?.TimeoutMs),
            AdditionalHeaders: additionalHeaders,
            ApiKey: GetPriority(options?.ApiKey, IdentityApiKeyEnvironmentVariable),
            Authorization: string.IsNullOrWhiteSpace(metricsKey)
                ? null
                : $"Basic {NormalizeBasicCredential(metricsKey)}"
        );
        ValidateExactlyOneAuthenticationHeader(configuration);
        return configuration;
    }

    public static ResolvedConfiguration Resolve(LocalHashingApiOptions? options)
    {
        var url = GetPriority(options?.Url, LocalHashingUrlEnvironmentVariable);
        if (string.IsNullOrWhiteSpace(url))
        {
            throw new ArgumentException(
                $"Local hashing URL is required. Specify in the constructor or set '{LocalHashingUrlEnvironmentVariable}' environment variable."
            );
        }

        return new ResolvedConfiguration(
            BaseUrl: url,
            TimeoutMs: GetTimeout(options?.TimeoutMs),
            AdditionalHeaders: GetAdditionalHeaders()
        );
    }

    private static string? GetPriority(string? explicitValue, string environmentVariable)
    {
        return explicitValue ?? Environment.GetEnvironmentVariable(environmentVariable);
    }

    private static string? GetPriorityOrMissing(string? explicitValue, string environmentVariable)
    {
        if (!string.IsNullOrWhiteSpace(explicitValue))
        {
            return explicitValue;
        }

        var environmentValue = Environment.GetEnvironmentVariable(environmentVariable);
        return string.IsNullOrWhiteSpace(environmentValue) ? null : environmentValue;
    }

    private static int GetTimeout(int? explicitTimeoutMs)
    {
        var rawValue =
            explicitTimeoutMs?.ToString()
            ?? Environment.GetEnvironmentVariable(TimeoutEnvironmentVariable);
        if (rawValue is null)
        {
            return DefaultTimeoutMs;
        }

        if (!int.TryParse(rawValue, out var timeoutMs))
        {
            throw new ArgumentException(
                $"Invalid timeout value in environment variable '{TimeoutEnvironmentVariable}': {rawValue}"
            );
        }

        return timeoutMs;
    }

    private static IReadOnlyDictionary<string, string> GetAdditionalHeaders()
    {
        var rawValue = Environment.GetEnvironmentVariable(AdditionalHeadersEnvironmentVariable);
        if (string.IsNullOrWhiteSpace(rawValue))
        {
            return new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        }

        using var document = JsonDocument.Parse(rawValue);
        if (document.RootElement.ValueKind != JsonValueKind.Object)
        {
            throw new ArgumentException(
                $"Environment variable '{AdditionalHeadersEnvironmentVariable}' must be a JSON object."
            );
        }

        var headers = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        foreach (var property in document.RootElement.EnumerateObject())
        {
            headers[property.Name] =
                property.Value.GetString()
                ?? throw new ArgumentException(
                    $"Environment variable '{AdditionalHeadersEnvironmentVariable}' must map header names to string values."
                );
        }

        return headers;
    }

    private static string NormalizeBasicCredential(string metricsKey)
    {
        var normalized = metricsKey.Trim();
        const string prefix = "Basic";
        if (
            normalized.StartsWith(prefix, StringComparison.OrdinalIgnoreCase)
            && normalized.Length > prefix.Length
            && char.IsWhiteSpace(normalized[prefix.Length])
        )
        {
            normalized = normalized[(prefix.Length + 1)..].TrimStart();
        }

        return normalized;
    }

    private static void ValidateExactlyOneAuthenticationHeader(ResolvedConfiguration configuration)
    {
        var hasApiKey =
            HasConfiguredValue(configuration.ApiKey)
            || HasConfiguredHeader(configuration.AdditionalHeaders, "x-api-key");
        var hasAuthorization =
            HasConfiguredValue(configuration.Authorization)
            || HasConfiguredHeader(configuration.AdditionalHeaders, "Authorization");

        if (hasApiKey == hasAuthorization)
        {
            throw new ArgumentException(
                "Exactly one authentication header must be configured: either 'x-api-key' or 'Authorization'."
            );
        }
    }

    private static bool HasConfiguredHeader(
        IReadOnlyDictionary<string, string> headers,
        string headerName
    ) => headers.TryGetValue(headerName, out var value) && HasConfiguredValue(value);

    private static bool HasConfiguredValue(string? value) => !string.IsNullOrWhiteSpace(value);
}
