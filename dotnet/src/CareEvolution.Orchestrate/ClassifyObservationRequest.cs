namespace CareEvolution.Orchestrate;

public sealed class ClassifyObservationRequest
{
    public required string Code { get; set; }

    public required string System { get; set; }

    public string? Display { get; set; }
}
