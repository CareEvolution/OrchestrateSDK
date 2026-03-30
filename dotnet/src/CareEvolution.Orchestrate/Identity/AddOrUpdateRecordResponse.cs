namespace CareEvolution.Orchestrate.Identity;

public sealed class AddOrUpdateRecordResponse : MatchedPersonReference
{
    public Advisories? Advisories { get; set; }
}
