using System.Text.Json.Serialization;

namespace CareEvolution.Orchestrate.Identity;

public sealed class MatchBlindedDemographicsResponse
{
    [JsonPropertyName("matchingPersons")]
    public List<Person> MatchingPersons { get; set; } = [];
}
