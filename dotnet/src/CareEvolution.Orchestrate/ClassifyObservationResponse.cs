namespace CareEvolution.Orchestrate;

public sealed class ClassifyObservationResponse
{
    public string? LoincComponent { get; set; }

    public string? LoincClass { get; set; }

    public string? LoincSystem { get; set; }

    public string? LoincMethodType { get; set; }

    public string? LoincTimeAspect { get; set; }

    public string? Covid19Lab { get; set; }

    public string? Category { get; set; }
}
