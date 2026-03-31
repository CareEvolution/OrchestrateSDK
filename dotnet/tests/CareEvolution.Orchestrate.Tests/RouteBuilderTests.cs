namespace CareEvolution.Orchestrate.Tests;

public sealed class RouteBuilderTests
{
    [Fact]
    public void BuildShouldReturnPathWhenQueryIsEmpty()
    {
        var route = RouteBuilder.Build(
            "/terminology/v1/fhir/r4/valueset",
            [new KeyValuePair<string, string?>("name", null)]
        );

        Assert.Equal("/terminology/v1/fhir/r4/valueset", route);
    }

    [Fact]
    public void BuildShouldCombineMultipleQuerySets()
    {
        var route = RouteBuilder.Build(
            "/convert/v1/hl7tofhirr4",
            [new KeyValuePair<string, string?>("patientId", "1234")],
            [
                new KeyValuePair<string, string?>("tz", "America/New_York"),
                new KeyValuePair<string, string?>("processingHint", "lab"),
            ]
        );

        Assert.Equal(
            "/convert/v1/hl7tofhirr4?patientId=1234&tz=America%2FNew_York&processingHint=lab",
            route
        );
    }

    [Fact]
    public void BuildQueryShouldSkipNullOrWhitespaceValues()
    {
        var query = RouteBuilder.BuildQuery([
            new KeyValuePair<string, string?>("name", "SNOMED"),
            new KeyValuePair<string, string?>("blank", ""),
            new KeyValuePair<string, string?>("spaces", "   "),
            new KeyValuePair<string, string?>("_count", "2"),
        ]);

        Assert.Equal("name=SNOMED&_count=2", query);
    }

    [Fact]
    public void BuildQueryShouldEscapeKeysAndValues()
    {
        var query = RouteBuilder.BuildQuery([
            new KeyValuePair<string, string?>("concept:contains", "heart failure/test"),
            new KeyValuePair<string, string?>("name", "SNOMED CT"),
        ]);

        Assert.Equal("concept%3Acontains=heart%20failure%2Ftest&name=SNOMED%20CT", query);
    }

    [Fact]
    public void EscapeShouldEscapeReservedCharacters()
    {
        var escaped = RouteBuilder.Escape("SNOMED/CT Demo");

        Assert.Equal("SNOMED%2FCT%20Demo", escaped);
    }
}
