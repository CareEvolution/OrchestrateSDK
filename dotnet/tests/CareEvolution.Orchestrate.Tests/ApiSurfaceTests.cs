using System.Text.Json;
using CareEvolution.Orchestrate.Tests.Helpers;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Options;

namespace CareEvolution.Orchestrate.Tests;

public sealed class ApiSurfaceTests
{
    [Fact]
    public async Task TerminologyBatchShouldPostToBatchRoute()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json("""{"items":[{"coding":[]}]}"""))
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        var response = await api.Terminology.StandardizeConditionAsync([
            new StandardizeRequest { Code = "123", System = "SNOMED" },
        ]);

        Assert.Single(response);
        Assert.NotNull(handler.LastRequest);
        Assert.Equal(
            "https://api.example.com/terminology/v1/standardize/condition/batch",
            handler.LastRequest!.RequestUri!.AbsoluteUri
        );
        Assert.Contains("\"items\"", handler.LastRequest.Body);
    }

    [Fact]
    public async Task ConvertHl7ShouldSendPlainTextAndQueryParameters()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json("{}"))
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        await api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request
            {
                Content = "MSH|^~\\&|",
                PatientId = "patient-1",
                PatientIdentifier = "identifier-1",
                PatientIdentifierSystem = "urn:test",
                Tz = "America/New_York",
                ProcessingHint = "lab",
            }
        );

        Assert.NotNull(handler.LastRequest);
        Assert.Equal(
            "https://api.example.com/convert/v1/hl7tofhirr4?patientId=patient-1&patientIdentifier=identifier-1&patientIdentifierSystem=urn%3Atest&tz=America%2FNew_York&processingHint=lab",
            handler.LastRequest!.RequestUri!.AbsoluteUri
        );
        Assert.Equal("text/plain", handler.LastRequest.Headers["Content-Type"].Single());
        Assert.Equal("MSH|^~\\&|", handler.LastRequest.Body);
    }

    [Fact]
    public async Task AdvancedTransportShouldApplyBaseUrlAndDeserializeJson()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json("""{"message":"ok"}"""))
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        var response = await api.HttpHandler.GetJsonAsync<TransportProbeResponse>(
            "/custom/v1/ping"
        );

        Assert.Equal("ok", response.Message);
        Assert.Equal(
            "https://api.example.com/custom/v1/ping",
            handler.LastRequest!.RequestUri!.AbsoluteUri
        );
        Assert.Same(httpClient, api.HttpHandler.HttpClient);
    }

    [Fact]
    public async Task AdvancedTransportShouldSupportTextResponses()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Text("<html></html>", "text/html"))
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        using var content = new StringContent("<ClinicalDocument />");
        var response = await api.HttpHandler.SendAsync<string>(
            HttpMethod.Post,
            "/custom/v1/render",
            content,
            "text/html"
        );

        Assert.Equal("<html></html>", response);
        Assert.Equal("text/html", handler.LastRequest!.Headers["Accept"].Single());
    }

    [Fact]
    public void AddOrchestrateApiShouldRegisterIOrchestrateApi()
    {
        var services = new ServiceCollection();

        services.AddOrchestrateApi(options =>
        {
            options.BaseUrl = "https://api.example.com";
            options.ApiKey = "test-api-key";
            options.TimeoutMs = 1234;
        });

        using var serviceProvider = services.BuildServiceProvider();
        var api = serviceProvider.GetRequiredService<IOrchestrateApi>();
        var options = serviceProvider
            .GetRequiredService<IOptions<OrchestrateClientOptions>>()
            .Value;

        Assert.NotNull(api);
        Assert.IsType<OrchestrateApi>(api);
        Assert.NotNull(api.Terminology);
        Assert.NotNull(api.Convert);
        Assert.NotNull(api.Insight);
        Assert.Equal("https://api.example.com", options.BaseUrl);
        Assert.Equal("test-api-key", options.ApiKey);
        Assert.Equal(1234, options.TimeoutMs);
    }

    [Fact]
    public async Task ConvertPdfShouldReturnBytes()
    {
        var expected = new byte[] { 1, 2, 3, 4 };
        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Bytes(expected, "application/pdf"))
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        var response = await api.Convert.CdaToPdfAsync(
            new ConvertCdaToPdfRequest { Content = "<ClinicalDocument />" }
        );

        Assert.Equal(expected, response);
        Assert.Equal("application/pdf", handler.LastRequest!.Headers["Accept"].Single());
    }

    [Fact]
    public async Task InsightRiskProfileShouldBuildExpectedQueryString()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Json("{}"))
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        await api.Insight.RiskProfileAsync(
            new InsightRiskProfileRequest
            {
                Content = new Bundle(),
                HccVersion = "24",
                PeriodEndDate = "2026-01-01",
                RaSegment = "community nondual aged",
            }
        );

        Assert.Equal(
            "https://api.example.com/insight/v1/riskprofile?hcc_version=24&period_end_date=2026-01-01&ra_segment=community%20nondual%20aged",
            handler.LastRequest!.RequestUri!.AbsoluteUri
        );
        Assert.Equal(
            "application/json; charset=utf-8",
            handler.LastRequest.Headers["Content-Type"].Single()
        );
    }

    [Fact]
    public async Task GetFhirR4CodeSystemShouldEscapePathSegment()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
                Task.FromResult(
                    FakeResponses.Json("""{"resourceType":"CodeSystem","concept":[]}""")
                )
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        _ = await api.Terminology.GetFhirR4CodeSystemAsync(
            new GetFhirR4CodeSystemRequest { CodeSystem = "SNOMED/CT Demo" }
        );

        Assert.Equal(
            "https://api.example.com/terminology/v1/fhir/r4/codesystem/SNOMED%2FCT%20Demo",
            handler.LastRequest!.RequestUri!.AbsoluteUri
        );
    }

    [Fact]
    public void CombinedFhirBundleFactoryShouldGenerateNdjson()
    {
        var request = ConvertRequestFactory.GenerateConvertCombinedFhirBundlesRequestFromBundles(
            [new Bundle(), new Bundle()],
            "person-1"
        );

        Assert.Equal("person-1", request.PatientId);
        Assert.Equal(1, request.Content.Count(character => character == '\n'));
        Assert.DoesNotContain("\"ResourceType\":", request.Content, StringComparison.Ordinal);
        Assert.Contains("\"resourceType\":\"Bundle\"", request.Content);
    }

    [Fact]
    public async Task StandardizeBundleShouldSerializeAsFhirJson()
    {
        Assert.Equal(Hl7.Fhir.Model.BundleType.BatchResponse, LiveTestData.R4Bundle.Type);
        Assert.NotEmpty(LiveTestData.R4Bundle.Entry);

        var handler = new FakeHttpMessageHandler(
            (_, _) =>
                Task.FromResult(
                    FakeResponses.Json(
                        """{"resourceType":"Bundle","type":"collection","entry":[]}"""
                    )
                )
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        await api.Terminology.StandardizeBundleAsync(LiveTestData.R4Bundle);

        Assert.NotNull(handler.LastRequest);
        Assert.Contains("\"resourceType\":\"Bundle\"", handler.LastRequest!.Body);
        Assert.DoesNotContain(
            "\"ResourceType\":",
            handler.LastRequest.Body,
            StringComparison.Ordinal
        );
        Assert.Contains("\"type\":\"batch-response\"", handler.LastRequest.Body);
    }

    [Fact]
    public async Task GetAllFhirR4ValueSetsForCodesShouldSerializeParametersWithValueString()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
                Task.FromResult(
                    FakeResponses.Json("""{"resourceType":"Parameters","parameter":[]}""")
                )
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        var parameters = new Parameters
        {
            Parameter =
            [
                new Parameters.ParameterComponent
                {
                    Name = "code",
                    Value = new Hl7.Fhir.Model.FhirString("119981000146107"),
                },
                new Parameters.ParameterComponent
                {
                    Name = "system",
                    Value = new Hl7.Fhir.Model.FhirString("http://snomed.info/sct"),
                },
            ],
        };

        await api.Terminology.GetAllFhirR4ValueSetsForCodesAsync(parameters);

        Assert.NotNull(handler.LastRequest);
        Assert.Contains("\"resourceType\":\"Parameters\"", handler.LastRequest!.Body);
        Assert.Contains("\"name\":\"code\"", handler.LastRequest.Body);
        Assert.Contains("\"valueString\":\"119981000146107\"", handler.LastRequest.Body);
        Assert.DoesNotContain(
            "\"ResourceType\":",
            handler.LastRequest.Body,
            StringComparison.Ordinal
        );
    }

    [Fact]
    public async Task ConvertFhirR4ToOmopShouldSerializeAsFhirJson()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Bytes([80, 75, 3, 4], "application/zip"))
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        _ = await api.Convert.FhirR4ToOmopAsync(
            new ConvertFhirR4ToOmopRequest { Content = LiveTestData.R4Bundle }
        );

        Assert.NotNull(handler.LastRequest);
        Assert.Contains("\"resourceType\":\"Bundle\"", handler.LastRequest!.Body);
        Assert.DoesNotContain(
            "\"ResourceType\":",
            handler.LastRequest.Body,
            StringComparison.Ordinal
        );
        Assert.Equal("application/zip", handler.LastRequest.Headers["Accept"].Single());
    }

    [Fact]
    public async Task ConvertFhirR4ToNemsisV35ShouldSerializeAsFhirJson()
    {
        var handler = new FakeHttpMessageHandler(
            (_, _) => Task.FromResult(FakeResponses.Text("<EMSDataSet />", "application/xml"))
        );
        using var httpClient = new HttpClient(handler);
        var api = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { BaseUrl = "https://api.example.com" }
        );

        _ = await api.Convert.FhirR4ToNemsisV35Async(
            new ConvertFhirR4ToNemsisV35Request { Content = LiveTestData.NemsisBundle }
        );

        Assert.NotNull(handler.LastRequest);
        Assert.Contains("\"resourceType\":\"Bundle\"", handler.LastRequest!.Body);
        Assert.DoesNotContain(
            "\"ResourceType\":",
            handler.LastRequest.Body,
            StringComparison.Ordinal
        );
        Assert.Equal("application/xml", handler.LastRequest.Headers["Accept"].Single());
    }

    private sealed class TransportProbeResponse
    {
        public string? Message { get; set; }
    }
}
