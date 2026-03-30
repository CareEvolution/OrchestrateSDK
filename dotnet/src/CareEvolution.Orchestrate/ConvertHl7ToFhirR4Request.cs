namespace CareEvolution.Orchestrate;

public sealed class ConvertHl7ToFhirR4Request
{
    public required string Content { get; set; }

    public string? PatientId { get; set; }

    public string? PatientIdentifier { get; set; }

    public string? PatientIdentifierSystem { get; set; }

    public string? Tz { get; set; }

    public string? ProcessingHint { get; set; }
}
