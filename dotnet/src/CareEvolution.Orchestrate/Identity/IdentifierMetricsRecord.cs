namespace CareEvolution.Orchestrate.Identity;

public sealed class IdentifierMetricsRecord
{
    public string? IdentifierType { get; set; }

    public int RecordCount { get; set; }

    public double RecordRatio { get; set; }

    public string? Source { get; set; }
}
