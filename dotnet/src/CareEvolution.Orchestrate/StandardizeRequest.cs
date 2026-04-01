namespace CareEvolution.Orchestrate;

public sealed class StandardizeRequest
{
    public string? Code { get; set; }

    public string? System { get; set; }

    public string? Display { get; set; }

    public string? TargetSystem { get; set; }
}
