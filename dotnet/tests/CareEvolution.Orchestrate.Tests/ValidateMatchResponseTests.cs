using System.Text.Json;
using CareEvolution.Orchestrate.Tests.Helpers;

namespace CareEvolution.Orchestrate.Tests;

public sealed class ValidateMatchResponseTests
{
    [Fact]
    public async Task ValidateMatchShouldDeserializeAllComparisonCategories()
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
    public async Task ValidateMatchShouldAllowAbsentComparison(
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
    public async Task ValidateMatchShouldAllowIncompleteComparison(string comparison)
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

        var response = await api.ValidateMatchAsync(
            new Demographic { FirstName = "SyntheticAlpha", HomePhoneNumber = "212-555-0175" },
            new Demographic { FirstName = "SyntheticBeta", Email = "synthetic@example.test" }
        );

        Assert.Equal(
            "https://identity.example.test/v1/validateMatch",
            handler.LastRequest!.RequestUri!.AbsoluteUri
        );
        Assert.Equal(HttpMethod.Post, handler.LastRequest.Method);
        using var body = JsonDocument.Parse(handler.LastRequest.Body!);
        Assert.Equal(2, body.RootElement.GetArrayLength());
        Assert.Equal("SyntheticAlpha", body.RootElement[0].GetProperty("firstName").GetString());
        Assert.Equal(
            "212-555-0175",
            body.RootElement[0].GetProperty("homePhoneNumber").GetString()
        );
        Assert.Equal("SyntheticBeta", body.RootElement[1].GetProperty("firstName").GetString());
        Assert.Equal(
            "synthetic@example.test",
            body.RootElement[1].GetProperty("email").GetString()
        );
        return response;
    }
}
