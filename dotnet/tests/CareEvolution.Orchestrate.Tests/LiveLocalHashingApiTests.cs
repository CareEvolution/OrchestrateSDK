using CareEvolution.Orchestrate.Tests.Helpers;

namespace CareEvolution.Orchestrate.Tests;

public sealed class LiveLocalHashingApiTests : IDisposable
{
    private readonly HttpClient _httpClient = new();
    private readonly LocalHashingApi _api;

    private static readonly Demographic Demographic = new()
    {
        FirstName = "John",
        LastName = "Doe",
        Dob = "1980-01-01",
        Gender = "male",
    };

    public LiveLocalHashingApiTests()
    {
        _api = LiveClients.CreateLocalHashingApi(_httpClient);
    }

    [LiveFact(LiveTestEnvironment.LocalHashingUrl)]
    public async Task HashShouldHashByDemographic()
    {
        var response = await _api.HashAsync(Demographic);

        Assert.True(response.Version > 0);
        Assert.Equal([], response.Advisories?.InvalidDemographicFields ?? []);
    }

    [LiveFact(LiveTestEnvironment.LocalHashingUrl)]
    public async Task HashWithInvalidDemographicFieldsShouldReturnAdvisories()
    {
        var response = await _api.HashAsync(
            new Demographic
            {
                FirstName = Demographic.FirstName,
                LastName = Demographic.LastName,
                Dob = "121980-01-01",
            }
        );

        Assert.True(response.Version > 0);
        Assert.Equal(["dob"], response.Advisories?.InvalidDemographicFields ?? []);
    }

    public void Dispose()
    {
        _httpClient.Dispose();
    }
}
