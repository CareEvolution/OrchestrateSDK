namespace CareEvolution.Orchestrate;

public sealed class ClassifyConditionRequest
{
    public required string Code { get; set; }

    public required string System { get; set; }

    public string? Display { get; set; }
}
