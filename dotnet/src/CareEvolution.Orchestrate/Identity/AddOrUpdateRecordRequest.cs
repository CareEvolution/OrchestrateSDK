namespace CareEvolution.Orchestrate.Identity;

public sealed class AddOrUpdateRecordRequest
{
    public required string Source { get; set; }

    public required string Identifier { get; set; }

    public required Demographic Demographic { get; set; }
}
