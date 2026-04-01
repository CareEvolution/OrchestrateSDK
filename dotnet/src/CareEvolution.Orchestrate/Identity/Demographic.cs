using System.Text.Json.Serialization;

namespace CareEvolution.Orchestrate.Identity;

public sealed class Demographic
{
    public string? FirstName { get; set; }

    public string? MiddleName { get; set; }

    public string? LastName { get; set; }

    public string? MaidenName { get; set; }

    public string? Gender { get; set; }

    public string? Race { get; set; }

    public string? HomePhoneNumber { get; set; }

    public string? CellPhoneNumber { get; set; }

    public string? Email { get; set; }

    public string? Dob { get; set; }

    public string? Street { get; set; }

    public string? City { get; set; }

    public string? State { get; set; }

    public string? ZipCode { get; set; }

    public string? Mrn { get; set; }

    public string? Hcid { get; set; }

    public string? Ssn { get; set; }

    [JsonPropertyName("medicaidID")]
    public string? MedicaidId { get; set; }
}
