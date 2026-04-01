namespace CareEvolution.Orchestrate;

public sealed class ConvertCdaToFhirR4Request
{
    public required string Content { get; set; }

    public string? PatientId { get; set; }

    public string? PatientIdentifier { get; set; }

    public string? PatientIdentifierSystem { get; set; }

    public bool? IncludeOriginalCda { get; set; }

    public bool? IncludeStandardizedCda { get; set; }
}
