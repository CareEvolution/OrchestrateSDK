using CareEvolution.Orchestrate.Tests.Helpers;

namespace CareEvolution.Orchestrate.Tests;

public sealed class ValidateMatchResponseTests
{
    [Fact]
    public async Task TransportShouldDeserializeAllComparisonCategories()
    {
        var response = await ReadResponseAsync(
            """
            {
                "result": "NO_MATCH",
                "noMatchReason": {
                    "exactFields": ["LastName"],
                    "highSimilarityFields": ["FirstName"],
                    "lowSimilarityFields": ["StreetName"],
                    "differentFields": ["DOB"],
                    "recordAMissingFields": ["Email"],
                    "recordBMissingFields": ["PhoneNumber"]
                }
            }
            """
        );

        Assert.Equal("NO_MATCH", response.Result);
        Assert.Null(response.MatchReason);
        var reason = Assert.IsType<ValidateMatchNoMatchReason>(response.NoMatchReason);
        Assert.Equal(["LastName"], reason.ExactFields);
        Assert.Equal(["FirstName"], reason.HighSimilarityFields);
        Assert.Equal(["StreetName"], reason.LowSimilarityFields);
        Assert.Equal(["DOB"], reason.DifferentFields);
        Assert.Equal(["Email"], reason.RecordAMissingFields);
        Assert.Equal(["PhoneNumber"], reason.RecordBMissingFields);
    }

    [Theory]
    [InlineData("""{"result":"NO_MATCH"}""", "NO_MATCH", null)]
    [InlineData("""{"result":"NO_MATCH","noMatchReason":null}""", "NO_MATCH", null)]
    [InlineData("""{"result":"MATCH","matchReason":"TestRule"}""", "MATCH", "TestRule")]
    public async Task TransportShouldAllowAbsentComparison(
        string json,
        string result,
        string? matchReason
    )
    {
        var response = await ReadResponseAsync(json);

        Assert.Equal(result, response.Result);
        Assert.Equal(matchReason, response.MatchReason);
        Assert.Null(response.NoMatchReason);
    }

    [Theory]
    [InlineData("""{}""")]
    [InlineData("""{"exactFields":null,"recordAMissingFields":null}""")]
    [InlineData("""{"differentFields":["DOB"]}""")]
    public async Task TransportShouldAllowIncompleteComparison(string comparison)
    {
        var response = await ReadResponseAsync(
            "{\"result\":\"NO_MATCH\",\"noMatchReason\":" + comparison + "}"
        );

        Assert.Equal("NO_MATCH", response.Result);
        var reason = Assert.IsType<ValidateMatchNoMatchReason>(response.NoMatchReason);
        Assert.Null(reason.ExactFields);
        Assert.Null(reason.RecordAMissingFields);
        Assert.Null(reason.RecordBMissingFields);
        if (comparison.Contains("differentFields"))
        {
            Assert.Equal(["DOB"], reason.DifferentFields);
        }
    }

    private static async Task<ValidateMatchResponse> ReadResponseAsync(string json)
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_IDENTITY_API_KEY"] = null,
                ["ORCHESTRATE_IDENTITY_METRICS_KEY"] = null,
                ["ORCHESTRATE_ADDITIONAL_HEADERS"] = null,
            }
        );
        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json(json))
        );
        using var httpClient = new HttpClient(handler);
        var api = new IdentityApi(
            httpClient,
            new IdentityApiOptions
            {
                Url = "https://identity.example.test",
                ApiKey = "test-api-key",
            }
        );

        return await api.Transport.PostJsonAsync<ValidateMatchResponse>(
            "/v1/validateMatch",
            new[] { new Demographic(), new Demographic() }
        );
    }
}
