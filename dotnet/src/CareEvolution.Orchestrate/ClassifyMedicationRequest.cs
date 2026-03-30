namespace CareEvolution.Orchestrate;

public sealed class ClassifyMedicationRequest
{
    public required string Code { get; set; }

    public required string System { get; set; }

    public string? Display { get; set; }
}
