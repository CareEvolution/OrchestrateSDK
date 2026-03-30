using System.ComponentModel;

namespace CareEvolution.Orchestrate.Identity;

public sealed class IdentityApi : IDisposable
{
    private readonly OrchestrateHttpClient _http;

    public IdentityApi(IdentityApiOptions? options = null)
        : this(httpClient: null, options) { }

    public IdentityApi(HttpClient? httpClient, IdentityApiOptions? options = null)
    {
        _http = new OrchestrateHttpClient(EnvironmentConfiguration.Resolve(options), httpClient);
        Monitoring = new IdentityMonitoringApi(_http);
    }

    public IdentityMonitoringApi Monitoring { get; }

    [EditorBrowsable(EditorBrowsableState.Advanced)]
    public IOrchestrateHttpClient Transport => _http;

    public HttpClient HttpClient => _http.HttpClient;

    public Task<AddOrUpdateRecordResponse> AddOrUpdateRecordAsync(
        AddOrUpdateRecordRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<AddOrUpdateRecordResponse>(
            $"/mpi/v1/record/{BuildSourceIdentifierRoute(request.Source, request.Identifier)}",
            request.Demographic,
            cancellationToken
        );

    public Task<MatchedPersonReference> AddOrUpdateBlindedRecordAsync(
        AddOrUpdateBlindedRecordRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<MatchedPersonReference>(
            $"/mpi/v1/blindedRecord/{BuildSourceIdentifierRoute(request.Source, request.Identifier)}",
            request.BlindedDemographic,
            cancellationToken
        );

    public Task<Person> GetPersonByRecordAsync(
        Record request,
        CancellationToken cancellationToken = default
    ) =>
        _http.GetJsonAsync<Person>(
            $"/mpi/v1/record/{BuildSourceIdentifierRoute(request.Source, request.Identifier)}",
            cancellationToken
        );

    public Task<Person> GetPersonByIdAsync(
        GetPersonByIdRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.GetJsonAsync<Person>(
            $"/mpi/v1/person/{RouteBuilder.Escape(request.Id)}",
            cancellationToken
        );

    public Task<MatchDemographicsResponse> MatchDemographicsAsync(
        Demographic request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<MatchDemographicsResponse>("/mpi/v1/match", request, cancellationToken);

    public Task<MatchBlindedDemographicsResponse> MatchBlindedDemographicsAsync(
        BlindedDemographic request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<MatchBlindedDemographicsResponse>(
            "/mpi/v1/matchBlinded",
            request,
            cancellationToken
        );

    public Task<DeleteRecordResponse> DeleteRecordAsync(
        Record request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<DeleteRecordResponse>(
            $"/mpi/v1/deleteRecord/{BuildSourceIdentifierRoute(request.Source, request.Identifier)}",
            new { },
            cancellationToken
        );

    public Task<AddMatchGuidanceResponse> AddMatchGuidanceAsync(
        AddMatchGuidanceRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<AddMatchGuidanceResponse>(
            "/mpi/v1/addGuidance",
            request,
            cancellationToken
        );

    public Task<RemoveMatchGuidanceResponse> RemoveMatchGuidanceAsync(
        MatchGuidanceRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<RemoveMatchGuidanceResponse>(
            "/mpi/v1/removeGuidance",
            request,
            cancellationToken
        );

    public void Dispose() => _http.Dispose();

    private static string BuildSourceIdentifierRoute(string source, string identifier) =>
        $"{RouteBuilder.Escape(source)}/{RouteBuilder.Escape(identifier)}";
}
