namespace CareEvolution.Orchestrate.Identity;

public sealed class DatasourceOverlapRecord
{
    public string? DatasourceA { get; set; }

    public string? DatasourceB { get; set; }

    public int OverlapCount { get; set; }
}
