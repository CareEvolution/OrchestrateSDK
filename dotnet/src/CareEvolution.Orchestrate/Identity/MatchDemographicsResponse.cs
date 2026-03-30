using System.Text.Json.Serialization;

namespace CareEvolution.Orchestrate.Identity;

public sealed class MatchDemographicsResponse
{
    [JsonPropertyName("matchingPersons")]
    public List<Person> MatchingPersons { get; set; } = [];

    public List<Advisories> Advisories { get; set; } = [];
}
