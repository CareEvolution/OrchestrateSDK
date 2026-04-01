namespace CareEvolution.Orchestrate;

public interface IInsightApi
{
    Task<Bundle> RiskProfileAsync(
        InsightRiskProfileRequest request,
        CancellationToken cancellationToken = default
    );
}

public sealed class InsightApi : IInsightApi
{
    private readonly OrchestrateHttpClient _http;

    internal InsightApi(OrchestrateHttpClient http)
    {
        _http = http;
    }

    public Task<Bundle> RiskProfileAsync(
        InsightRiskProfileRequest request,
        CancellationToken cancellationToken = default
    )
    {
        var route = RouteBuilder.Build(
            "/insight/v1/riskprofile",
            [
                new KeyValuePair<string, string?>("hcc_version", request.HccVersion),
                new KeyValuePair<string, string?>("period_end_date", request.PeriodEndDate),
                new KeyValuePair<string, string?>("ra_segment", request.RaSegment),
            ]
        );
        return _http.PostJsonAsync<Bundle>(route, request.Content, cancellationToken);
    }
}
