namespace CareEvolution.Orchestrate.Identity;

public sealed class IdentityMonitoringApi
{
    private readonly OrchestrateHttpClient _http;

    internal IdentityMonitoringApi(OrchestrateHttpClient http)
    {
        _http = http;
    }

    public Task<IdentifierMetricsResponse> IdentifierMetricsAsync(
        CancellationToken cancellationToken = default
    ) =>
        _http.GetJsonAsync<IdentifierMetricsResponse>(
            "/monitoring/v1/identifierMetrics",
            cancellationToken
        );

    public Task<OverlapMetricsResponse> OverlapMetricsAsync(
        CancellationToken cancellationToken = default
    ) =>
        _http.GetJsonAsync<OverlapMetricsResponse>(
            "/monitoring/v1/overlapMetrics",
            cancellationToken
        );
}
