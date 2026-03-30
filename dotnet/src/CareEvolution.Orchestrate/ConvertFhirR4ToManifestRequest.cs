namespace CareEvolution.Orchestrate;

public sealed class ConvertFhirR4ToManifestRequest
{
    public required Bundle Content { get; set; }

    public string? Delimiter { get; set; }

    public string? Source { get; set; }

    public string? PatientIdentifier { get; set; }

    public string? Setting { get; set; }
}
