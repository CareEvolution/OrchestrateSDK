namespace CareEvolution.Orchestrate.Identity;

/// <summary>
/// Field comparisons for a failed stateless /v1/validateMatch request.
/// Record A is the first demographic; record B is the second.
/// Comparison categories may be omitted or null.
/// </summary>
public sealed class ValidateMatchNoMatchReason
{
    public List<string>? ExactFields { get; set; }

    public List<string>? HighSimilarityFields { get; set; }

    public List<string>? LowSimilarityFields { get; set; }

    public List<string>? DifferentFields { get; set; }

    public List<string>? RecordAMissingFields { get; set; }

    public List<string>? RecordBMissingFields { get; set; }
}
