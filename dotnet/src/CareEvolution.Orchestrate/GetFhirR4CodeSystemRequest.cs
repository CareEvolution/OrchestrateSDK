namespace CareEvolution.Orchestrate;

public sealed class GetFhirR4CodeSystemRequest
{
    public required string CodeSystem { get; set; }

    public int? PageNumber { get; set; }

    public int? PageSize { get; set; }

    public string? ConceptContains { get; set; }
}
