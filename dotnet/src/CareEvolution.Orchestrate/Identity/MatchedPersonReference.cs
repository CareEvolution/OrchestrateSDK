namespace CareEvolution.Orchestrate.Identity;

public class MatchedPersonReference
{
    public Person? MatchedPerson { get; set; }

    public List<Person> ChangedPersons { get; set; } = [];
}
