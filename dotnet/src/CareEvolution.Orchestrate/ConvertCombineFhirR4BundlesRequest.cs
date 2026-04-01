namespace CareEvolution.Orchestrate;

public sealed class ConvertCombineFhirR4BundlesRequest
{
    public required string Content { get; set; }

    public string? PatientId { get; set; }

    public string? PatientIdentifier { get; set; }

    public string? PatientIdentifierSystem { get; set; }
}
