using System.Text.Json.Serialization;

namespace CareEvolution.Orchestrate;

public sealed class ClassifyConditionResponse
{
    [JsonPropertyName("ccsrCatgory")]
    public CodeableConcept? CcsrCategory { get; set; }

    public Coding? CcsrDefaultInpatient { get; set; }

    public Coding? CcsrDefaultOutpatient { get; set; }

    public bool CciChronic { get; set; }

    public bool CciAcute { get; set; }

    public CodeableConcept? HccCategory { get; set; }

    public bool Behavioral { get; set; }

    public bool Substance { get; set; }

    public bool SocialDeterminant { get; set; }

    public string? Covid19Condition { get; set; }
}
