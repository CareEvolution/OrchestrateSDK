namespace CareEvolution.Orchestrate;

public sealed class InsightRiskProfileRequest
{
    public required Bundle Content { get; set; }

    public string? HccVersion { get; set; }

    public string? PeriodEndDate { get; set; }

    public string? RaSegment { get; set; }
}
