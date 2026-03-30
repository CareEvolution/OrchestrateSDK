using CareEvolution.Orchestrate.Tests.Helpers;

namespace CareEvolution.Orchestrate.Tests;

public sealed class LiveIdentityApiTests
{
    private static readonly IdentityApi Api = LiveClients.CreateIdentityApi();
    private const string DefaultSource = "source";

    private static readonly Demographic Demographic = new()
    {
        FirstName = "John",
        LastName = "Doe",
        Dob = "1980-01-01",
        Gender = "male",
    };

    private static readonly BlindedDemographic BlindedDemographic = new()
    {
        Data = LiveTestData.BlindedDemographicData,
        Version = 1,
    };

    [LiveFact(LiveTestEnvironment.IdentityApiKey, LiveTestEnvironment.IdentityUrl)]
    public async Task AddOrUpdateRecordShouldAddRecord()
    {
        var response = await Api.AddOrUpdateRecordAsync(
            new AddOrUpdateRecordRequest
            {
                Source = DefaultSource,
                Identifier = Guid.NewGuid().ToString(),
                Demographic = Demographic,
            }
        );

        Assert.NotNull(response.MatchedPerson?.Id);
    }

    [LiveFact(LiveTestEnvironment.IdentityApiKey, LiveTestEnvironment.IdentityUrl)]
    public async Task AddOrUpdateRecordWithUrlUnsafeIdentifierShouldAddRecord()
    {
        var response = await Api.AddOrUpdateRecordAsync(
            new AddOrUpdateRecordRequest
            {
                Source = DefaultSource,
                Identifier = $"{Guid.NewGuid()}/",
                Demographic = Demographic,
            }
        );

        Assert.NotNull(response.MatchedPerson?.Id);
    }

    [LiveFact(LiveTestEnvironment.IdentityApiKey, LiveTestEnvironment.IdentityUrl)]
    public async Task AddOrUpdateBlindedRecordShouldAddRecord()
    {
        var response = await Api.AddOrUpdateBlindedRecordAsync(
            new AddOrUpdateBlindedRecordRequest
            {
                Source = DefaultSource,
                Identifier = Guid.NewGuid().ToString(),
                BlindedDemographic = BlindedDemographic,
            }
        );

        Assert.NotNull(response.MatchedPerson?.Id);
    }

    [LiveFact(LiveTestEnvironment.IdentityApiKey, LiveTestEnvironment.IdentityUrl)]
    public async Task AddOrUpdateBlindedRecordWithUrlUnsafeIdentifierShouldAddRecord()
    {
        var response = await Api.AddOrUpdateBlindedRecordAsync(
            new AddOrUpdateBlindedRecordRequest
            {
                Source = DefaultSource,
                Identifier = $"{Guid.NewGuid()}+/=",
                BlindedDemographic = BlindedDemographic,
            }
        );

        Assert.NotNull(response.MatchedPerson?.Id);
    }

    [LiveFact(LiveTestEnvironment.IdentityApiKey, LiveTestEnvironment.IdentityUrl)]
    public async Task GetPersonByRecordShouldMatch()
    {
        var (person, identifier) = await CreateRandomRecordAsync();
        var response = await Api.GetPersonByRecordAsync(
            new CareEvolution.Orchestrate.Identity.Record
            {
                Source = DefaultSource,
                Identifier = identifier,
            }
        );
        Assert.Equal(person.Id, response.Id);
    }

    [LiveFact(LiveTestEnvironment.IdentityApiKey, LiveTestEnvironment.IdentityUrl)]
    public async Task GetPersonByIdShouldMatch()
    {
        var (person, _) = await CreateRandomRecordAsync();
        var response = await Api.GetPersonByIdAsync(new GetPersonByIdRequest { Id = person.Id });
        Assert.Equal(person.Id, response.Id);
    }

    [LiveFact(LiveTestEnvironment.IdentityApiKey, LiveTestEnvironment.IdentityUrl)]
    public async Task MatchDemographicsShouldMatch()
    {
        var response = await Api.MatchDemographicsAsync(Demographic);
        Assert.NotNull(response);
        Assert.NotNull(response.MatchingPersons);
    }

    [LiveFact(LiveTestEnvironment.IdentityApiKey, LiveTestEnvironment.IdentityUrl)]
    public async Task MatchBlindedDemographicsShouldMatch()
    {
        var response = await Api.MatchBlindedDemographicsAsync(BlindedDemographic);
        Assert.NotNull(response);
        Assert.NotNull(response.MatchingPersons);
    }

    [LiveFact(LiveTestEnvironment.IdentityApiKey, LiveTestEnvironment.IdentityUrl)]
    public async Task DeleteRecordShouldDelete()
    {
        var (person, identifier) = await CreateRandomRecordAsync();
        var response = await Api.DeleteRecordAsync(
            new CareEvolution.Orchestrate.Identity.Record
            {
                Source = DefaultSource,
                Identifier = identifier,
            }
        );

        Assert.Contains(response.ChangedPersons, changedPerson => changedPerson.Id == person.Id);
        Assert.Contains(
            response.ChangedPersons.SelectMany(changedPerson => changedPerson.Records),
            record => record.Source == DefaultSource && record.Identifier == identifier
        );
    }

    [LiveFact(LiveTestEnvironment.IdentityApiKey, LiveTestEnvironment.IdentityUrl)]
    public async Task AddMatchGuidanceShouldReportChangedPersons()
    {
        var (firstPerson, firstIdentifier) = await CreateRandomRecordAsync();
        var (secondPerson, secondIdentifier) = await CreateRandomRecordAsync();

        var response = await Api.AddMatchGuidanceAsync(
            new AddMatchGuidanceRequest
            {
                RecordOne = new CareEvolution.Orchestrate.Identity.Record
                {
                    Source = DefaultSource,
                    Identifier = firstIdentifier,
                },
                RecordTwo = new CareEvolution.Orchestrate.Identity.Record
                {
                    Source = DefaultSource,
                    Identifier = secondIdentifier,
                },
                Action = "Match",
                Comment = "Testing",
            }
        );

        Assert.Contains(
            response.ChangedPersons,
            person => person.Id == firstPerson.Id || person.Id == secondPerson.Id
        );
    }

    [LiveFact(LiveTestEnvironment.IdentityApiKey, LiveTestEnvironment.IdentityUrl)]
    public async Task RemoveMatchGuidanceShouldSeparatePersons()
    {
        var (firstPerson, firstIdentifier) = await CreateRandomRecordAsync();
        var (secondPerson, secondIdentifier) = await CreateRandomRecordAsync();
        var recordOne = new CareEvolution.Orchestrate.Identity.Record
        {
            Source = DefaultSource,
            Identifier = firstIdentifier,
        };
        var recordTwo = new CareEvolution.Orchestrate.Identity.Record
        {
            Source = DefaultSource,
            Identifier = secondIdentifier,
        };

        await Api.AddMatchGuidanceAsync(
            new AddMatchGuidanceRequest
            {
                RecordOne = recordOne,
                RecordTwo = recordTwo,
                Action = "Match",
                Comment = "Adding for removal testing",
            }
        );

        var response = await Api.RemoveMatchGuidanceAsync(
            new MatchGuidanceRequest
            {
                RecordOne = recordOne,
                RecordTwo = recordTwo,
                Comment = "Removal testing",
            }
        );

        Assert.Contains(
            response.ChangedPersons,
            person => person.Id == firstPerson.Id || person.Id == secondPerson.Id
        );
    }

    [LiveFact(
        LiveTestEnvironment.IdentityApiKey,
        LiveTestEnvironment.IdentityUrl,
        LiveTestEnvironment.IdentityMetricsKey
    )]
    public async Task MonitoringIdentifierMetricsShouldHaveMetrics()
    {
        await CreateRandomRecordAsync();
        var response = await Api.Monitoring.IdentifierMetricsAsync();

        Assert.False(string.IsNullOrWhiteSpace(response.Refreshed));
        Assert.True(response.TotalRecordCount > 0);
        Assert.True(response.TotalPersonCount > 0);
        Assert.NotNull(response.GlobalMetricsRecords);
        Assert.Equal(string.Empty, response.GlobalMetricsRecords[0].Source);
        Assert.Contains(response.SummaryMetricsRecords, record => record.Source == DefaultSource);
        Assert.True(response.SourceTotals[0].TotalRecordCount > 0);
    }

    [LiveFact(
        LiveTestEnvironment.IdentityApiKey,
        LiveTestEnvironment.IdentityUrl,
        LiveTestEnvironment.IdentityMetricsKey
    )]
    public async Task MonitoringOverlapMetricsShouldHaveMetrics()
    {
        await CreateRandomRecordAsync();
        await CreateRandomRecordAsync();

        var response = await Api.Monitoring.OverlapMetricsAsync();
        Assert.NotNull(response.DatasourceOverlapRecords);
        Assert.Contains(
            response.DatasourceOverlapRecords,
            record => record.DatasourceA == DefaultSource
        );
        Assert.Contains(
            response.DatasourceOverlapRecords,
            record => record.DatasourceB == DefaultSource
        );
        Assert.True(response.DatasourceOverlapRecords[0].OverlapCount > 0);
    }

    private static async Task<(Person Person, string Identifier)> CreateRandomRecordAsync()
    {
        var identifier = Guid.NewGuid().ToString();
        var response = await Api.AddOrUpdateRecordAsync(
            new AddOrUpdateRecordRequest
            {
                Source = DefaultSource,
                Identifier = identifier,
                Demographic = Demographic,
            }
        );
        return (response.MatchedPerson!, identifier);
    }
}
