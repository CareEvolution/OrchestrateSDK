namespace CareEvolution.Orchestrate.Identity;

public sealed class Person
{
    public required string Id { get; set; }

    public List<Record> Records { get; set; } = [];

    public int Version { get; set; }

    public PersonStatus? Status { get; set; }
}
