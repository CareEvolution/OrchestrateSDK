namespace CareEvolution.Orchestrate.Identity;

/// <summary>Stateless /v1/validateMatch response, with optional match diagnostics.</summary>
public sealed class ValidateMatchResponse
{
    public required string Result { get; set; }

    public string? MatchReason { get; set; }

    public ValidateMatchNoMatchReason? NoMatchReason { get; set; }
}
