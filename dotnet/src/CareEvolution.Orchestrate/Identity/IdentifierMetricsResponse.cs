namespace CareEvolution.Orchestrate.Identity;

public sealed class IdentifierMetricsResponse
{
    public string? Refreshed { get; set; }

    public int TotalRecordCount { get; set; }

    public int TotalPersonCount { get; set; }

    public List<IdentifierMetricsRecord> GlobalMetricsRecords { get; set; } = [];

    public List<IdentifierMetricsRecord> SummaryMetricsRecords { get; set; } = [];

    public List<SourceTotal> SourceTotals { get; set; } = [];
}
