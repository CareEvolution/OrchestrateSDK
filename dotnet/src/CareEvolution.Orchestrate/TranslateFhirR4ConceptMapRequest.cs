namespace CareEvolution.Orchestrate;

public sealed class TranslateFhirR4ConceptMapRequest
{
    public required string Code { get; set; }

    public string? Domain { get; set; }
}
