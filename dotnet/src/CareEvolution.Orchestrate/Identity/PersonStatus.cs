namespace CareEvolution.Orchestrate.Identity;

public sealed class PersonStatus
{
    public string? Code { get; set; }

    public List<string> SupersededBy { get; set; } = [];
}
