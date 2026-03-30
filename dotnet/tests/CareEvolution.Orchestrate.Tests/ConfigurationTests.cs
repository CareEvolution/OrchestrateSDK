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
        using var api = new OrchestrateApi(
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
    public void OrchestrateApiShouldThrowForInvalidTimeoutEnvironmentVariable()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?> { ["ORCHESTRATE_TIMEOUT_MS"] = "not-a-number" }
        );

        var exception = Assert.Throws<ArgumentException>(() => new OrchestrateApi());
        Assert.Contains("ORCHESTRATE_TIMEOUT_MS", exception.Message);
    }

    [Fact]
    public void IdentityApiShouldRequireUrl()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?> { ["ORCHESTRATE_IDENTITY_URL"] = null }
        );

        var exception = Assert.Throws<ArgumentException>(() => new IdentityApi());
        Assert.Contains("Identity URL is required", exception.Message);
    }

    [Theory]
    [InlineData("metrics-key", "Basic metrics-key")]
    [InlineData("Basic metrics-key", "Basic metrics-key")]
    public async Task IdentityApiShouldNormalizeMetricsKey(
        string rawMetricsKey,
        string expectedAuthorization
    )
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_IDENTITY_URL"] = "https://identity.example.com",
            }
        );

        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json("""{"datasourceOverlapRecords":[]}"""))
        );
        using var httpClient = new HttpClient(handler);
        using var api = new IdentityApi(
            httpClient,
            new IdentityApiOptions { MetricsKey = rawMetricsKey }
        );

        await api.Monitoring.OverlapMetricsAsync();

        Assert.NotNull(handler.LastRequest);
        Assert.Equal(expectedAuthorization, handler.LastRequest!.Headers["Authorization"].Single());
    }

    [Fact]
    public async Task HttpErrorsShouldBeConvertedToOrchestrateClientErrors()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
                Task.FromResult(
                    FakeResponses.Json(
                        """{"issue":[{"severity":"error","code":"invalid","diagnostics":"Expected a Bundle but found a Patient"}]}""",
                        HttpStatusCode.BadRequest
                    )
                )
        );

        using var httpClient = new HttpClient(handler);
        using var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        var exception = await Assert.ThrowsAsync<OrchestrateClientError>(() =>
            api.Terminology.StandardizeConditionAsync(
                new StandardizeRequest { Code = "123", System = "SNOMED" }
            )
        );

        Assert.Contains(
            "error: invalid - Expected a Bundle but found a Patient",
            exception.Message
        );
        Assert.Equal(HttpStatusCode.BadRequest, exception.StatusCode);
    }
}
