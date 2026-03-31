using CareEvolution.Orchestrate.Tests.Helpers;

namespace CareEvolution.Orchestrate.Tests;

public sealed class IdentityApiTests
{
    [Fact]
    public async Task AddOrUpdateRecordShouldEncodeRouteAndSendDemographicPayload()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
                Task.FromResult(
                    FakeResponses.Json(
                        """{"matchedPerson":{"id":"1","records":[],"version":1,"status":{"code":"Active","supersededBy":[]}},"changedPersons":[],"advisories":{"invalidDemographicFields":[]}}"""
                    )
                )
        );
        using var httpClient = new HttpClient(handler);
        var api = new IdentityApi(
            httpClient,
            new IdentityApiOptions { Url = "https://identity.example.com" }
        );

        await api.AddOrUpdateRecordAsync(
            new AddOrUpdateRecordRequest
            {
                Source = "source one",
                Identifier = "id+/=",
                Demographic = new Demographic
                {
                    FirstName = "John",
                    LastName = "Doe",
                    MedicaidId = "12345",
                },
            }
        );

        Assert.Equal(
            "https://identity.example.com/mpi/v1/record/source%20one/id%2B%2F%3D",
            handler.LastRequest!.RequestUri!.AbsoluteUri
        );
        Assert.Contains("\"firstName\":\"John\"", handler.LastRequest.Body);
        Assert.Contains("\"medicaidID\":\"12345\"", handler.LastRequest.Body);
    }

    [Fact]
    public async Task AddOrUpdateBlindedRecordShouldFlattenPayload()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
                Task.FromResult(
                    FakeResponses.Json(
                        """{"matchedPerson":{"id":"1","records":[],"version":1,"status":{"code":"Active","supersededBy":[]}},"changedPersons":[]}"""
                    )
                )
        );
        using var httpClient = new HttpClient(handler);
        var api = new IdentityApi(
            httpClient,
            new IdentityApiOptions { Url = "https://identity.example.com" }
        );

        await api.AddOrUpdateBlindedRecordAsync(
            new AddOrUpdateBlindedRecordRequest
            {
                Source = "source",
                Identifier = "identifier",
                BlindedDemographic = new BlindedDemographic { Data = "abc", Version = 1 },
            }
        );

        Assert.DoesNotContain(
            "blindedDemographic",
            handler.LastRequest!.Body,
            StringComparison.OrdinalIgnoreCase
        );
        Assert.Contains("\"data\":\"abc\"", handler.LastRequest.Body);
    }

    [Fact]
    public async Task DeleteRecordShouldSendEmptyObjectPayload()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json("""{"changedPersons":[]}"""))
        );
        using var httpClient = new HttpClient(handler);
        var api = new IdentityApi(
            httpClient,
            new IdentityApiOptions { Url = "https://identity.example.com" }
        );

        await api.DeleteRecordAsync(
            new CareEvolution.Orchestrate.Identity.Record
            {
                Source = "source",
                Identifier = "identifier",
            }
        );

        Assert.Equal("{}", handler.LastRequest!.Body);
    }

    [Fact]
    public async Task MonitoringShouldCallExpectedRoute()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
                Task.FromResult(
                    FakeResponses.Json(
                        """{"refreshed":"2026-01-01T00:00:00Z","totalRecordCount":1,"totalPersonCount":1,"globalMetricsRecords":[],"summaryMetricsRecords":[],"sourceTotals":[]}"""
                    )
                )
        );
        using var httpClient = new HttpClient(handler);
        var api = new IdentityApi(
            httpClient,
            new IdentityApiOptions { Url = "https://identity.example.com" }
        );

        var response = await api.Monitoring.IdentifierMetricsAsync();

        Assert.Equal(1, response.TotalRecordCount);
        Assert.Equal(
            "https://identity.example.com/monitoring/v1/identifierMetrics",
            handler.LastRequest!.RequestUri!.AbsoluteUri
        );
    }

    [Fact]
    public async Task LocalHashingShouldUseConfiguredUrl()
    {
        using var environment = new EnvironmentVariableScope(
            new Dictionary<string, string?>
            {
                ["ORCHESTRATE_IDENTITY_LOCAL_HASHING_URL"] = "https://hashing.example.com",
            }
        );

        var handler = new FakeHttpMessageHandler(
            (_, _) =>
                Task.FromResult(
                    FakeResponses.Json(
                        """{"data":"abc","version":1,"advisories":{"invalidDemographicFields":[]}}"""
                    )
                )
        );
        using var httpClient = new HttpClient(handler);
        var api = new LocalHashingApi(httpClient);

        var response = await api.HashAsync(new Demographic { FirstName = "John" });

        Assert.Equal("abc", response.Data);
        Assert.Equal(
            "https://hashing.example.com/hash",
            handler.LastRequest!.RequestUri!.AbsoluteUri
        );
    }
}
