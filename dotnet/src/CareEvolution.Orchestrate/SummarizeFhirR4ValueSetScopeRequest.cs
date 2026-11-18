namespace CareEvolution.Orchestrate;

public sealed class SummarizeFhirR4ValueSetScopeRequest
{
    public required string Scope { get; set; }

    public int? PageNumber { get; set; }

    public int? PageSize { get; set; }
}
