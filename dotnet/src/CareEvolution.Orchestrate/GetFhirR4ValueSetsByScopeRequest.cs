namespace CareEvolution.Orchestrate;

public sealed class GetFhirR4ValueSetsByScopeRequest
{
    public string? Name { get; set; }

    public int? PageNumber { get; set; }

    public int? PageSize { get; set; }

    public string? Scope { get; set; }
}
