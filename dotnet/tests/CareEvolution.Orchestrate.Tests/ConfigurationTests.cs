using System.Net;
using CareEvolution.Orchestrate.Exceptions;
using CareEvolution.Orchestrate.Tests.Helpers;

namespace CareEvolution.Orchestrate.Tests;

public sealed class ConfigurationTests
{
    [Fact]
    public async Task OrchestrateApiShouldPreferConstructorValuesOverEnvironmentVariables()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_BASE_URL"] = "https://env.example.com",
                ["ORCHESTRATE_API_KEY"] = "env-api-key",
                ["ORCHESTRATE_TIMEOUT_MS"] = "45000",
                ["ORCHESTRATE_ADDITIONAL_HEADERS"] =
                    """{"x-custom-header":"custom-value","x-api-key":"wrong"}""",
            }
        );

        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json("""{"coding":[]}"""))
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions
            {
                ApiKey = "constructor-api-key",
                BaseUrl = "https://constructor.example.com",
                TimeoutMs = 30000,
            }
        );

        await api.Terminology.StandardizeConditionAsync(
            new StandardizeRequest { Code = "123", System = "SNOMED" }
        );

        Assert.NotNull(handler.LastRequest);
        Assert.Equal(
            "https://constructor.example.com/terminology/v1/standardize/condition",
            handler.LastRequest!.RequestUri!.ToString()
        );
        Assert.Equal("constructor-api-key", handler.LastRequest.Headers["x-api-key"].Single());
        Assert.Equal("custom-value", handler.LastRequest.Headers["x-custom-header"].Single());
        Assert.Equal("application/json", handler.LastRequest.Headers["Accept"].Single());
    }

    [Fact]
    public async Task OrchestrateApiShouldTreatWhitespaceBaseUrlAsMissing()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_BASE_URL"] = "https://env.example.com",
                ["ORCHESTRATE_API_KEY"] = "env-api-key",
                ["ORCHESTRATE_ADDITIONAL_HEADERS"] = null,
            }
        );

        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json("""{"coding":[]}"""))
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(httpClient, new OrchestrateClientOptions { BaseUrl = "   " });

        await api.Terminology.StandardizeConditionAsync(
            new StandardizeRequest { Code = "123", System = "SNOMED" }
        );

        Assert.Equal(
            "https://env.example.com/terminology/v1/standardize/condition",
            handler.LastRequest!.RequestUri!.ToString()
        );
    }

    [Fact]
    public void OrchestrateApiShouldThrowForInvalidTimeoutEnvironmentVariable()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?> { ["ORCHESTRATE_TIMEOUT_MS"] = "not-a-number" }
        );

        using var httpClient = new HttpClient(
            new FakeHttpMessageHandler((_, _) => throw new NotImplementedException())
        );
        var exception = Assert.Throws<ArgumentException>(() => new OrchestrateApi(httpClient));
        Assert.Contains("ORCHESTRATE_TIMEOUT_MS", exception.Message);
    }

    [Fact]
    public void OrchestrateApiShouldRequireExactlyOneAuthenticationHeader()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_API_KEY"] = null,
                ["ORCHESTRATE_ADDITIONAL_HEADERS"] = null,
            }
        );

        using var httpClient = new HttpClient(
            new FakeHttpMessageHandler((_, _) => throw new NotImplementedException())
        );
        var exception = Assert.Throws<ArgumentException>(() => new OrchestrateApi(httpClient));

        Assert.Contains("Exactly one authentication header", exception.Message);
    }

    [Fact]
    public void OrchestrateApiShouldThrowWhenBothAuthenticationHeadersAreConfigured()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_API_KEY"] = "env-api-key",
                ["ORCHESTRATE_ADDITIONAL_HEADERS"] = """{"Authorization":"Bearer token"}""",
            }
        );

        using var httpClient = new HttpClient(
            new FakeHttpMessageHandler((_, _) => throw new NotImplementedException())
        );
        var exception = Assert.Throws<ArgumentException>(() => new OrchestrateApi(httpClient));

        Assert.Contains("Exactly one authentication header", exception.Message);
    }

    [Fact]
    public async Task OrchestrateApiShouldAllowAuthorizationFromAdditionalHeaders()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_API_KEY"] = null,
                ["ORCHESTRATE_ADDITIONAL_HEADERS"] = """{"Authorization":"Bearer token"}""",
            }
        );

        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json("""{"coding":[]}"""))
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        await api.Terminology.StandardizeConditionAsync(
            new StandardizeRequest { Code = "123", System = "SNOMED" }
        );

        Assert.Equal("Bearer token", handler.LastRequest!.Headers["Authorization"].Single());
        Assert.False(handler.LastRequest.Headers.ContainsKey("x-api-key"));
    }

    [Fact]
    public void IdentityApiShouldRequireUrl()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?> { ["ORCHESTRATE_IDENTITY_URL"] = null }
        );

        using var httpClient = new HttpClient(
            new FakeHttpMessageHandler((_, _) => throw new NotImplementedException())
        );
        var exception = Assert.Throws<ArgumentException>(() => new IdentityApi(httpClient));
        Assert.Contains("Identity URL is required", exception.Message);
    }

    [Theory]
    [InlineData("metrics-key", "Basic metrics-key")]
    [InlineData("Basic metrics-key", "Basic metrics-key")]
    [InlineData("basic metrics-key", "Basic metrics-key")]
    [InlineData("  Basic   metrics-key  ", "Basic metrics-key")]
    public async Task IdentityApiShouldNormalizeMetricsKey(
        string rawMetricsKey,
        string expectedAuthorization
    )
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_IDENTITY_URL"] = "https://identity.example.com",
                ["ORCHESTRATE_IDENTITY_API_KEY"] = null,
            }
        );

        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json("""{"datasourceOverlapRecords":[]}"""))
        );
        using var httpClient = new HttpClient(handler);
        var api = new IdentityApi(
            httpClient,
            new IdentityApiOptions { MetricsKey = rawMetricsKey }
        );

        await api.Monitoring.OverlapMetricsAsync();

        Assert.NotNull(handler.LastRequest);
        Assert.Equal(expectedAuthorization, handler.LastRequest!.Headers["Authorization"].Single());
    }

    [Fact]
    public void IdentityApiShouldRequireExactlyOneAuthenticationHeader()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_IDENTITY_URL"] = "https://identity.example.com",
                ["ORCHESTRATE_IDENTITY_API_KEY"] = null,
                ["ORCHESTRATE_IDENTITY_METRICS_KEY"] = null,
                ["ORCHESTRATE_ADDITIONAL_HEADERS"] = null,
            }
        );

        using var httpClient = new HttpClient(
            new FakeHttpMessageHandler((_, _) => throw new NotImplementedException())
        );
        var exception = Assert.Throws<ArgumentException>(() => new IdentityApi(httpClient));

        Assert.Contains("Exactly one authentication header", exception.Message);
    }

    [Fact]
    public void IdentityApiShouldThrowWhenBothAuthenticationHeadersAreConfigured()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_IDENTITY_URL"] = "https://identity.example.com",
                ["ORCHESTRATE_IDENTITY_API_KEY"] = "identity-api-key",
                ["ORCHESTRATE_IDENTITY_METRICS_KEY"] = "metrics-key",
            }
        );

        using var httpClient = new HttpClient(
            new FakeHttpMessageHandler((_, _) => throw new NotImplementedException())
        );
        var exception = Assert.Throws<ArgumentException>(() => new IdentityApi(httpClient));

        Assert.Contains("Exactly one authentication header", exception.Message);
    }

    [Fact]
    public async Task HttpErrorsShouldBeConvertedToOrchestrateClientExceptions()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_API_KEY"] = null,
                ["ORCHESTRATE_ADDITIONAL_HEADERS"] = null,
            }
        );

        var handler = new FakeHttpMessageHandler(
            (_, _) =>
                Task.FromResult(
                    FakeResponses.Json(
                        """{"resourceType":"OperationOutcome","issue":[{"severity":"error","code":"invalid","diagnostics":"Expected a Bundle but found a Patient"}]}""",
                        HttpStatusCode.BadRequest
                    )
                )
        );

        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions
            {
                BaseUrl = "https://api.example.com",
                ApiKey = "test-api-key",
            }
        );

        var exception = await Assert.ThrowsAsync<OrchestrateClientException>(() =>
            api.Terminology.StandardizeConditionAsync(
                new StandardizeRequest { Code = "123", System = "SNOMED" }
            )
        );

        Assert.Contains(
            "error: invalid - Expected a Bundle but found a Patient",
            exception.Message
        );
        Assert.Equal(HttpStatusCode.BadRequest, exception.StatusCode);
        Assert.NotNull(exception.OperationOutcome);
        Assert.Single(exception.OperationOutcome!.Issue);
    }

    [Fact]
    public async Task MultipleIssueOperationOutcomeShouldExposeAllStructuredIssues()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_API_KEY"] = null,
                ["ORCHESTRATE_ADDITIONAL_HEADERS"] = null,
            }
        );

        const string responseJson = """
            {
              "resourceType": "OperationOutcome",
              "issue": [
                {
                  "severity": "error",
                  "code": "invalid",
                  "diagnostics": "Missing recordTarget in ClinicalDocument"
                },
                {
                  "severity": "information",
                  "code": "informational",
                  "details": {
                    "coding": [{ "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAProcessingMessage", "code": "DocumentId" }],
                    "text": "fb04306a-0834-432d-90c3-251ed7d3401d"
                  }
                },
                {
                  "severity": "information",
                  "code": "informational",
                  "details": {
                    "coding": [{ "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAProcessingMessage", "code": "DocumentEffectiveTime" }],
                    "text": "2011-05-27T01:44:27-05:00"
                  }
                }
              ]
            }
            """;

        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json(responseJson, HttpStatusCode.BadRequest))
        );

        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions
            {
                BaseUrl = "https://api.example.com",
                ApiKey = "test-api-key",
            }
        );

        var exception = await Assert.ThrowsAsync<OrchestrateClientException>(() =>
            api.Convert.CdaToFhirR4Async(
                new ConvertCdaToFhirR4Request { Content = "<ClinicalDocument/>" }
            )
        );

        Assert.Equal(HttpStatusCode.BadRequest, exception.StatusCode);
        Assert.NotNull(exception.OperationOutcome);
        Assert.Equal(3, exception.OperationOutcome!.Issue.Count);
        Assert.Equal(3, exception.Issues.Count);

        // Error issue: diagnostics only, no details
        Assert.Contains(
            "error: invalid - Missing recordTarget in ClinicalDocument",
            exception.Issues[0]
        );

        // Information issues: details.text extracted
        Assert.Contains("fb04306a-0834-432d-90c3-251ed7d3401d", exception.Issues[1]);
        Assert.Contains("2011-05-27T01:44:27-05:00", exception.Issues[2]);

        // Message covers all issues
        Assert.Contains("Missing recordTarget in ClinicalDocument", exception.Message);
        Assert.Contains("fb04306a-0834-432d-90c3-251ed7d3401d", exception.Message);
        Assert.Contains("2011-05-27T01:44:27-05:00", exception.Message);
    }

    [Fact]
    public async Task MalformedJsonHttpErrorsShouldPreserveRawResponseText()
    {
        const string responseText = """{"oops":""";
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
                Task.FromResult(
                    FakeResponses.Text(responseText, "application/json", HttpStatusCode.BadRequest)
                )
        );

        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions
            {
                BaseUrl = "https://api.example.com",
                ApiKey = "test-api-key",
            }
        );

        var exception = await Assert.ThrowsAsync<OrchestrateClientException>(() =>
            api.Terminology.StandardizeConditionAsync(
                new StandardizeRequest { Code = "123", System = "SNOMED" }
            )
        );

        Assert.Equal(responseText, exception.ResponseText);
        Assert.Contains(responseText, exception.Issues);
        Assert.Contains(responseText, exception.Message);
        Assert.Null(exception.OperationOutcome);
    }
}
