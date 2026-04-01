namespace CareEvolution.Orchestrate;

public sealed class ConvertX12ToFhirR4Request
{
    public required string Content { get; set; }

    public string? PatientId { get; set; }

    public string? PatientIdentifier { get; set; }

    public string? PatientIdentifierSystem { get; set; }
}
