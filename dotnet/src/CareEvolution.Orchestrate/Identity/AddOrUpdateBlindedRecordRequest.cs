namespace CareEvolution.Orchestrate.Identity;

public sealed class AddOrUpdateBlindedRecordRequest
{
    public required string Source { get; set; }

    public required string Identifier { get; set; }

    public required BlindedDemographic BlindedDemographic { get; set; }
}
