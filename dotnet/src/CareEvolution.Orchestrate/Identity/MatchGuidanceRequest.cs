namespace CareEvolution.Orchestrate.Identity;

public class MatchGuidanceRequest
{
    public required Record RecordOne { get; set; }

    public required Record RecordTwo { get; set; }

    public required string Comment { get; set; }
}
