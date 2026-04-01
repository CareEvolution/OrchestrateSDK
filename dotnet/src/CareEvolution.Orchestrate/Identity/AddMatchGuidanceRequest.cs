namespace CareEvolution.Orchestrate.Identity;

public sealed class AddMatchGuidanceRequest : MatchGuidanceRequest
{
    public required string Action { get; set; }
}
