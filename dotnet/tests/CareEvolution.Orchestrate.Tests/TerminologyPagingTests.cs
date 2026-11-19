using System.Net;
using System.Text.Json;
using CareEvolution.Orchestrate.Exceptions;
using CareEvolution.Orchestrate.Tests.Helpers;
using CodeSystem = Hl7.Fhir.Model.R4.CodeSystem;

namespace CareEvolution.Orchestrate.Tests;

public sealed class TerminologyPagingTests
{
    public static TheoryData<string> Routes =>
        new()
        {
            "codesystem",
            "code-system-summaries",
            "conceptmaps",
            "valuesets",
            "scope-summaries",
        };

    public static TheoryData<string> ExplicitRoutes => new() { "codesystem", "valuesets" };
    public static TheoryData<string> BundleRoutes =>
        new() { "code-system-summaries", "conceptmaps", "valuesets", "scope-summaries" };

    [Theory]
    [MemberData(nameof(ExplicitRoutes))]
    public async Task IncompletePagingShouldFailBeforeHttp(string route)
    {
        foreach (var paging in new (int? PageNumber, int? PageSize)[] { (0, null), (null, 2) })
        {
            var handler = new FakeHttpMessageHandler(
                (_, _) => throw new InvalidOperationException("Unexpected HTTP request")
            );
            using var http = new HttpClient(handler);

            var error = await Assert.ThrowsAsync<ArgumentException>(() =>
                Call(Api(http), route, paging.PageNumber, paging.PageSize)
            );

            Assert.Contains("pageNumber and pageSize must be provided together", error.Message);
            Assert.Null(handler.LastRequest);
        }
    }

    [Theory]
    [MemberData(nameof(ExplicitRoutes))]
    public async Task ExplicitPagingShouldReturnOnlyRequestedPage(string route)
    {
        foreach (var pageNumber in new[] { 0, 3 })
        {
            var requests = new List<Uri>();
            var handler = new FakeHttpMessageHandler(
                (request, _) =>
                {
                    requests.Add(request.RequestUri!);
                    return Task.FromResult(
                        FakeResponses.Json(Page(route, ["one"], next: "/unused"))
                    );
                }
            );
            using var http = new HttpClient(handler);

            var result = await Call(Api(http), route, pageNumber, 2);

            Assert.Equal(["one"], Ids(result));
            if (result is Bundle explicitBundle)
                Assert.Equal(
                    ["self", "next", "alternate"],
                    explicitBundle.Link.Select(link => link.Relation)
                );
            Assert.Single(requests);
            AssertRequest(requests[0], route, pageNumber, 2);
        }
    }

    [Theory]
    [InlineData(false)]
    [InlineData(true)]
    public async Task CodeSystemShouldAggregateConceptsWithNumberedPages(bool knownCount)
    {
        var requests = new List<Uri>();
        var pages = new Queue<string>([
            Page("codesystem", ["one"], knownCount ? 2 : null),
            Page("codesystem", ["two"]),
            Page("codesystem", []),
        ]);
        var handler = new FakeHttpMessageHandler(
            (request, _) =>
            {
                requests.Add(request.RequestUri!);
                return Task.FromResult(FakeResponses.Json(pages.Dequeue()));
            }
        );
        using var http = new HttpClient(handler);
        var result = Assert.IsType<CodeSystem>(await Call(Api(http), "codesystem"));
        Assert.Equal(["one", "two"], Ids(result));
        Assert.Equal("resource-id", result.Id);
        Assert.Equal(knownCount ? 2 : (int?)null, result.Count);
        Assert.Equal(knownCount ? 2 : 3, requests.Count);
        for (var index = 0; index < requests.Count; index++)
            AssertRequest(requests[index], "codesystem", index, 10000);
    }

    [Theory]
    [MemberData(nameof(BundleRoutes))]
    public async Task BundleShouldFollowNextLinksRegardlessOfCountsOrEmptyPages(string route)
    {
        foreach (
            var next in new[]
            {
                "/continuation?cursor=a%2Bb",
                "https://example.test/continuation?cursor=a%2Bb",
            }
        )
        {
            var requests = new List<Uri>();
            var pages = new Queue<string>([
                Page(route, [], 0, next),
                Page(route, ["one"], next: "?cursor=last%2Ftoken"),
                Page(route, ["two"]),
            ]);
            var handler = new FakeHttpMessageHandler(
                (request, _) =>
                {
                    requests.Add(request.RequestUri!);
                    return Task.FromResult(FakeResponses.Json(pages.Dequeue()));
                }
            );
            using var http = new HttpClient(handler);
            var result = Assert.IsType<Bundle>(await Call(Api(http), route));
            Assert.Equal(["one", "two"], Ids(result));
            Assert.Equal("resource-id", result.Id);
            Assert.Equal(0, result.Total);
            var link = Assert.Single(result.Link);
            Assert.Equal("alternate", link.Relation);
            Assert.Equal("https://example.test/catalog", link.Url);
            Assert.Equal(3, requests.Count);
            AssertRequest(requests[0], route, 0, 10000);
            Assert.Equal("https://example.test/continuation?cursor=a%2Bb", requests[1].AbsoluteUri);
            Assert.Equal(
                "https://example.test/continuation?cursor=last%2Ftoken",
                requests[2].AbsoluteUri
            );
        }
    }

    [Theory]
    [MemberData(nameof(BundleRoutes))]
    public async Task BundleWithoutNextLinkShouldStopEvenWhenTotalSuggestsMore(string route)
    {
        var calls = 0;
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
            {
                calls++;
                return Task.FromResult(FakeResponses.Json(Page(route, ["one"], 999)));
            }
        );
        using var http = new HttpClient(handler);
        Assert.Equal(["one"], Ids(await Call(Api(http), route)));
        Assert.Equal(1, calls);
    }

    [Theory]
    [InlineData("https://other.example/next")]
    [InlineData("http://example.test/next")]
    public async Task NextLinkToDifferentOriginShouldFailBeforeSendingCredentials(string next)
    {
        var calls = 0;
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
            {
                calls++;
                return Task.FromResult(FakeResponses.Json(Page("valuesets", [], next: next)));
            }
        );
        using var http = new HttpClient(handler);
        await Assert.ThrowsAsync<ArgumentException>(() => Call(Api(http), "valuesets"));
        Assert.Equal(1, calls);
    }

    [Theory]
    [MemberData(nameof(Routes))]
    public async Task AutomaticPagingShouldStopOnEmptyFirstPage(string route)
    {
        var calls = 0;
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
            {
                calls++;
                return Task.FromResult(FakeResponses.Json(Page(route, [])));
            }
        );
        using var http = new HttpClient(handler);

        Assert.Empty(Ids(await Call(Api(http), route)));
        Assert.Equal(1, calls);
    }

    [Theory]
    [MemberData(nameof(Routes))]
    public async Task AutomaticPagingShouldPropagateLaterErrors(string route)
    {
        var calls = 0;
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
                Task.FromResult(
                    ++calls == 1
                        ? FakeResponses.Json(Page(route, ["one"], next: "/next"))
                        : FakeResponses.Json("{}", HttpStatusCode.InternalServerError)
                )
        );
        using var http = new HttpClient(handler);

        await Assert.ThrowsAsync<OrchestrateClientException>(() => Call(Api(http), route));
        Assert.Equal(2, calls);
    }

    [Theory]
    [MemberData(nameof(Routes))]
    public async Task AutomaticPagingShouldHonorCancellationBetweenPages(string route)
    {
        using var cancellation = new CancellationTokenSource();
        var calls = 0;
        var handler = new FakeHttpMessageHandler(
            (_, _) =>
            {
                calls++;
                cancellation.Cancel();
                return Task.FromResult(FakeResponses.Json(Page(route, ["one"], next: "/next")));
            }
        );
        using var http = new HttpClient(handler);

        await Assert.ThrowsAnyAsync<OperationCanceledException>(() =>
            Call(Api(http), route, cancellationToken: cancellation.Token)
        );
        Assert.Equal(1, calls);
    }

    private static OrchestrateApi Api(HttpClient http) =>
        new(
            http,
            new OrchestrateClientOptions { BaseUrl = "https://example.test", ApiKey = "test-key" }
        );

    private static async Task<object> Call(
        OrchestrateApi api,
        string route,
        int? pageNumber = null,
        int? pageSize = null,
        CancellationToken cancellationToken = default
    ) =>
        route switch
        {
            "codesystem" => await api.Terminology.GetFhirR4CodeSystemAsync(
                new()
                {
                    CodeSystem = "LOINC",
                    ConceptContains = "blood pressure",
                    PageNumber = pageNumber,
                    PageSize = pageSize,
                },
                cancellationToken
            ),
            "code-system-summaries" => await api.Terminology.SummarizeFhirR4CodeSystemsAsync(
                cancellationToken
            ),
            "conceptmaps" => await api.Terminology.GetFhirR4ConceptMapsAsync(cancellationToken),
            "valuesets" => await api.Terminology.GetFhirR4ValueSetsByScopeAsync(
                new()
                {
                    Name = "test name",
                    Scope = "http://loinc.org",
                    PageNumber = pageNumber,
                    PageSize = pageSize,
                },
                cancellationToken
            ),
            "scope-summaries" => await api.Terminology.SummarizeFhirR4ValueSetScopeAsync(
                new() { Scope = "http://loinc.org" },
                cancellationToken
            ),
            _ => throw new ArgumentOutOfRangeException(nameof(route)),
        };

    private static IEnumerable<string?> Ids(object result) =>
        result switch
        {
            CodeSystem codeSystem => codeSystem.Concept.Select(concept => concept.Code),
            Bundle bundle => bundle.Entry.Select(entry => entry.Resource.Id),
            _ => throw new ArgumentException("Unexpected response", nameof(result)),
        };

    private static string Page(string route, string[] ids, int? total = null, string? next = null)
    {
        var resource = new Dictionary<string, object?> { ["id"] = "resource-id" };
        if (route == "codesystem")
        {
            resource["resourceType"] = "CodeSystem";
            resource["concept"] = ids.Select(id => new { code = id });
            if (total is not null)
                resource["count"] = total;
        }
        else
        {
            resource["resourceType"] = "Bundle";
            var links = new List<object>
            {
                new { relation = "self", url = "https://example.test/page/0" },
            };
            if (next is not null)
                links.Add(new { relation = "next", url = next });
            links.Add(new { relation = "alternate", url = "https://example.test/catalog" });
            resource["link"] = links;
            resource["entry"] = ids.Select(id => new
            {
                resource = new { resourceType = "ValueSet", id },
            });
            if (total is not null)
                resource["total"] = total;
        }
        return JsonSerializer.Serialize(resource);
    }

    private static void AssertRequest(Uri uri, string route, int pageNumber, int pageSize)
    {
        var path = route switch
        {
            "codesystem" => "/codesystem/LOINC",
            "code-system-summaries" => "/codesystem",
            "conceptmaps" => "/conceptmap",
            _ => "/valueset",
        };
        Assert.Equal($"/terminology/v1/fhir/r4{path}", uri.AbsolutePath);
        var query = uri
            .Query.TrimStart('?')
            .Split('&')
            .Select(pair => pair.Split('=', 2))
            .ToDictionary(
                pair => Uri.UnescapeDataString(pair[0]),
                pair => Uri.UnescapeDataString(pair[1])
            );
        var expected = new Dictionary<string, string>
        {
            ["page.num"] = pageNumber.ToString(),
            ["_count"] = pageSize.ToString(),
        };
        if (route == "codesystem")
            expected["concept:contains"] = "blood pressure";
        if (route is "code-system-summaries" or "scope-summaries")
            expected["_summary"] = "true";
        if (route is "valuesets" or "scope-summaries")
            expected["extension.scope"] = "http://loinc.org";
        if (route == "valuesets")
            expected["name"] = "test name";
        Assert.Equal(expected.OrderBy(pair => pair.Key), query.OrderBy(pair => pair.Key));
    }
}
