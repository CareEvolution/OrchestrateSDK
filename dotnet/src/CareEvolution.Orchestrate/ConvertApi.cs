using System.Net.Http;

namespace CareEvolution.Orchestrate;

public interface IConvertApi
{
    Task<Bundle> CdaToFhirR4Async(
        ConvertCdaToFhirR4Request request,
        CancellationToken cancellationToken = default
    );
    Task<string> CdaToHtmlAsync(
        ConvertCdaToHtmlRequest request,
        CancellationToken cancellationToken = default
    );
    Task<byte[]> CdaToPdfAsync(
        ConvertCdaToPdfRequest request,
        CancellationToken cancellationToken = default
    );
    Task<Bundle> CombineFhirR4BundlesAsync(
        ConvertCombineFhirR4BundlesRequest request,
        CancellationToken cancellationToken = default
    );
    Task<Bundle> FhirDstu2ToFhirR4Async(
        ConvertFhirDstu2ToFhirR4Request request,
        CancellationToken cancellationToken = default
    );
    Task<string> FhirR4ToCdaAsync(
        ConvertFhirR4ToCdaRequest request,
        CancellationToken cancellationToken = default
    );
    Task<Bundle> FhirR4ToHealthLakeAsync(
        ConvertFhirR4ToHealthLakeRequest request,
        CancellationToken cancellationToken = default
    );
    Task<byte[]> FhirR4ToManifestAsync(
        ConvertFhirR4ToManifestRequest request,
        CancellationToken cancellationToken = default
    );
    Task<string> FhirR4ToNemsisV34Async(
        ConvertFhirR4ToNemsisV34Request request,
        CancellationToken cancellationToken = default
    );
    Task<string> FhirR4ToNemsisV35Async(
        ConvertFhirR4ToNemsisV35Request request,
        CancellationToken cancellationToken = default
    );
    Task<byte[]> FhirR4ToOmopAsync(
        ConvertFhirR4ToOmopRequest request,
        CancellationToken cancellationToken = default
    );
    Task<Bundle> FhirStu3ToFhirR4Async(
        ConvertFhirStu3ToFhirR4Request request,
        CancellationToken cancellationToken = default
    );
    Task<Bundle> Hl7ToFhirR4Async(
        ConvertHl7ToFhirR4Request request,
        CancellationToken cancellationToken = default
    );
    Task<Bundle> X12ToFhirR4Async(
        ConvertX12ToFhirR4Request request,
        CancellationToken cancellationToken = default
    );
}

public sealed class ConvertApi : IConvertApi
{
    private readonly OrchestrateHttpClient _http;

    internal ConvertApi(OrchestrateHttpClient http)
    {
        _http = http;
    }

    public Task<Bundle> Hl7ToFhirR4Async(
        ConvertHl7ToFhirR4Request request,
        CancellationToken cancellationToken = default
    )
    {
        var route = RouteBuilder.Build(
            "/convert/v1/hl7tofhirr4",
            [
                new KeyValuePair<string, string?>("patientId", request.PatientId),
                new KeyValuePair<string, string?>("patientIdentifier", request.PatientIdentifier),
                new KeyValuePair<string, string?>(
                    "patientIdentifierSystem",
                    request.PatientIdentifierSystem
                ),
                new KeyValuePair<string, string?>("tz", request.Tz),
                new KeyValuePair<string, string?>("processingHint", request.ProcessingHint),
            ]
        );
        return PostTextForJsonAsync<Bundle>(
            route,
            request.Content,
            "text/plain",
            cancellationToken
        );
    }

    public Task<Bundle> CdaToFhirR4Async(
        ConvertCdaToFhirR4Request request,
        CancellationToken cancellationToken = default
    )
    {
        var route = RouteBuilder.Build(
            "/convert/v1/cdatofhirr4",
            [
                new KeyValuePair<string, string?>("patientId", request.PatientId),
                new KeyValuePair<string, string?>("patientIdentifier", request.PatientIdentifier),
                new KeyValuePair<string, string?>(
                    "patientIdentifierSystem",
                    request.PatientIdentifierSystem
                ),
                new KeyValuePair<string, string?>(
                    "includeOriginalCda",
                    request.IncludeOriginalCda?.ToString()?.ToLowerInvariant()
                ),
                new KeyValuePair<string, string?>(
                    "includeStandardizedCda",
                    request.IncludeStandardizedCda?.ToString()?.ToLowerInvariant()
                ),
            ]
        );
        return PostTextForJsonAsync<Bundle>(
            route,
            request.Content,
            "application/xml",
            cancellationToken
        );
    }

    public Task<byte[]> CdaToPdfAsync(
        ConvertCdaToPdfRequest request,
        CancellationToken cancellationToken = default
    ) =>
        PostTextAsync<byte[]>(
            "/convert/v1/cdatopdf",
            request.Content,
            "application/xml",
            "application/pdf",
            ResponseKind.Bytes,
            cancellationToken
        );

    public Task<string> FhirR4ToCdaAsync(
        ConvertFhirR4ToCdaRequest request,
        CancellationToken cancellationToken = default
    ) =>
        PostJsonAsync<string>(
            "/convert/v1/fhirr4tocda",
            request.Content,
            "application/xml",
            ResponseKind.Text,
            cancellationToken
        );

    public Task<byte[]> FhirR4ToOmopAsync(
        ConvertFhirR4ToOmopRequest request,
        CancellationToken cancellationToken = default
    ) =>
        PostJsonAsync<byte[]>(
            "/convert/v1/fhirr4toomop",
            request.Content,
            "application/zip",
            ResponseKind.Bytes,
            cancellationToken
        );

    public Task<Bundle> CombineFhirR4BundlesAsync(
        ConvertCombineFhirR4BundlesRequest request,
        CancellationToken cancellationToken = default
    )
    {
        var route = RouteBuilder.Build(
            "/convert/v1/combinefhirr4bundles",
            [
                new KeyValuePair<string, string?>("patientId", request.PatientId),
                new KeyValuePair<string, string?>("patientIdentifier", request.PatientIdentifier),
                new KeyValuePair<string, string?>(
                    "patientIdentifierSystem",
                    request.PatientIdentifierSystem
                ),
            ]
        );
        return PostTextForJsonAsync<Bundle>(
            route,
            request.Content,
            "application/x-ndjson",
            cancellationToken
        );
    }

    public Task<Bundle> X12ToFhirR4Async(
        ConvertX12ToFhirR4Request request,
        CancellationToken cancellationToken = default
    )
    {
        var route = RouteBuilder.Build(
            "/convert/v1/x12tofhirr4",
            [
                new KeyValuePair<string, string?>("patientId", request.PatientId),
                new KeyValuePair<string, string?>("patientIdentifier", request.PatientIdentifier),
                new KeyValuePair<string, string?>(
                    "patientIdentifierSystem",
                    request.PatientIdentifierSystem
                ),
            ]
        );
        return PostTextForJsonAsync<Bundle>(
            route,
            request.Content,
            "text/plain",
            cancellationToken
        );
    }

    public Task<Bundle> FhirDstu2ToFhirR4Async(
        ConvertFhirDstu2ToFhirR4Request request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<Bundle>(
            "/convert/v1/fhirdstu2tofhirr4",
            request.Content,
            cancellationToken
        );

    public Task<Bundle> FhirStu3ToFhirR4Async(
        ConvertFhirStu3ToFhirR4Request request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<Bundle>(
            "/convert/v1/fhirstu3tofhirr4",
            request.Content,
            cancellationToken
        );

    public Task<Bundle> FhirR4ToHealthLakeAsync(
        ConvertFhirR4ToHealthLakeRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<Bundle>(
            "/convert/v1/fhirr4tohealthlake",
            request.Content,
            cancellationToken
        );

    public Task<string> CdaToHtmlAsync(
        ConvertCdaToHtmlRequest request,
        CancellationToken cancellationToken = default
    ) =>
        PostTextAsync<string>(
            "/convert/v1/cdatohtml",
            request.Content,
            "application/xml",
            "text/html",
            ResponseKind.Text,
            cancellationToken
        );

    public Task<string> FhirR4ToNemsisV34Async(
        ConvertFhirR4ToNemsisV34Request request,
        CancellationToken cancellationToken = default
    ) =>
        PostJsonAsync<string>(
            "/convert/v1/fhirr4tonemsisv34",
            request.Content,
            "application/xml",
            ResponseKind.Text,
            cancellationToken
        );

    public Task<string> FhirR4ToNemsisV35Async(
        ConvertFhirR4ToNemsisV35Request request,
        CancellationToken cancellationToken = default
    ) =>
        PostJsonAsync<string>(
            "/convert/v1/fhirr4tonemsisv35",
            request.Content,
            "application/xml",
            ResponseKind.Text,
            cancellationToken
        );

    public Task<byte[]> FhirR4ToManifestAsync(
        ConvertFhirR4ToManifestRequest request,
        CancellationToken cancellationToken = default
    )
    {
        var route = RouteBuilder.Build(
            "/convert/v1/fhirr4tomanifest",
            [
                new KeyValuePair<string, string?>("delimiter", request.Delimiter),
                new KeyValuePair<string, string?>("source", request.Source),
                new KeyValuePair<string, string?>("patientIdentifier", request.PatientIdentifier),
                new KeyValuePair<string, string?>("setting", request.Setting),
            ]
        );
        return PostJsonAsync<byte[]>(
            route,
            request.Content,
            "application/zip",
            ResponseKind.Bytes,
            cancellationToken
        );
    }

    private Task<T> PostTextForJsonAsync<T>(
        string route,
        string content,
        string contentType,
        CancellationToken cancellationToken
    ) =>
        PostTextAsync<T>(
            route,
            content,
            contentType,
            "application/json",
            ResponseKind.Json,
            cancellationToken
        );

    private Task<T> PostTextAsync<T>(
        string route,
        string content,
        string contentType,
        string accept,
        ResponseKind responseKind,
        CancellationToken cancellationToken
    )
    {
        var httpContent = new StringContent(content);
        httpContent.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue(
            contentType
        );
        return _http.PostAsync<T>(route, httpContent, accept, responseKind, cancellationToken);
    }

    private Task<T> PostJsonAsync<T>(
        string route,
        Bundle content,
        string accept,
        ResponseKind responseKind,
        CancellationToken cancellationToken
    )
    {
        var httpContent = OrchestrateHttpClient.CreateJsonContent(content);
        return _http.PostAsync<T>(route, httpContent, accept, responseKind, cancellationToken);
    }
}
