namespace CareEvolution.Orchestrate;

public sealed class ClassifyMedicationResponse
{
    public List<string> MedRtTherapeuticClass { get; set; } = [];

    public List<string> RxNormIngredient { get; set; } = [];

    public string? RxNormStrength { get; set; }

    public bool RxNormGeneric { get; set; }

    public string? Covid19Rx { get; set; }
}
