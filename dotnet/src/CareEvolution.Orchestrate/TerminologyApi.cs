namespace CareEvolution.Orchestrate;

public interface ITerminologyApi
{
    Task<ClassifyConditionResponse> ClassifyConditionAsync(
        ClassifyConditionRequest request,
        CancellationToken cancellationToken = default
    );
    Task<IReadOnlyList<ClassifyConditionResponse>> ClassifyConditionAsync(
        IReadOnlyList<ClassifyConditionRequest> request,
        CancellationToken cancellationToken = default
    );
    Task<ClassifyMedicationResponse> ClassifyMedicationAsync(
        ClassifyMedicationRequest request,
        CancellationToken cancellationToken = default
    );
    Task<IReadOnlyList<ClassifyMedicationResponse>> ClassifyMedicationAsync(
        IReadOnlyList<ClassifyMedicationRequest> request,
        CancellationToken cancellationToken = default
    );
    Task<ClassifyObservationResponse> ClassifyObservationAsync(
        ClassifyObservationRequest request,
        CancellationToken cancellationToken = default
    );
    Task<IReadOnlyList<ClassifyObservationResponse>> ClassifyObservationAsync(
        IReadOnlyList<ClassifyObservationRequest> request,
        CancellationToken cancellationToken = default
    );
    Task<Parameters> GetAllFhirR4ValueSetsForCodesAsync(
        Parameters request,
        CancellationToken cancellationToken = default
    );
    Task<CodeSystem> GetFhirR4CodeSystemAsync(
        GetFhirR4CodeSystemRequest request,
        CancellationToken cancellationToken = default
    );
    Task<Bundle> GetFhirR4ConceptMapsAsync(CancellationToken cancellationToken = default);
    Task<ValueSet> GetFhirR4ValueSetAsync(
        GetFhirR4ValueSetRequest request,
        CancellationToken cancellationToken = default
    );
    Task<Bundle> GetFhirR4ValueSetsByScopeAsync(
        GetFhirR4ValueSetsByScopeRequest request,
        CancellationToken cancellationToken = default
    );
    Task<ValueSet> GetFhirR4ValueSetScopesAsync(CancellationToken cancellationToken = default);
    Task<Bundle> StandardizeBundleAsync(
        Bundle bundle,
        CancellationToken cancellationToken = default
    );
    Task<StandardizeResponse> StandardizeConditionAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    );
    Task<IReadOnlyList<StandardizeResponse>> StandardizeConditionAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    );
    Task<StandardizeResponse> StandardizeLabAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    );
    Task<IReadOnlyList<StandardizeResponse>> StandardizeLabAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    );
    Task<StandardizeResponse> StandardizeMedicationAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    );
    Task<IReadOnlyList<StandardizeResponse>> StandardizeMedicationAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    );
    Task<StandardizeResponse> StandardizeObservationAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    );
    Task<IReadOnlyList<StandardizeResponse>> StandardizeObservationAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    );
    Task<StandardizeResponse> StandardizeProcedureAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    );
    Task<IReadOnlyList<StandardizeResponse>> StandardizeProcedureAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    );
    Task<StandardizeResponse> StandardizeRadiologyAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    );
    Task<IReadOnlyList<StandardizeResponse>> StandardizeRadiologyAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    );
    Task<CodeSystem> SummarizeFhirR4CodeSystemAsync(
        SummarizeFhirR4CodeSystemRequest request,
        CancellationToken cancellationToken = default
    );
    Task<Bundle> SummarizeFhirR4CodeSystemsAsync(CancellationToken cancellationToken = default);
    Task<ValueSet> SummarizeFhirR4ValueSetAsync(
        SummarizeFhirR4ValueSetRequest request,
        CancellationToken cancellationToken = default
    );
    Task<Bundle> SummarizeFhirR4ValueSetScopeAsync(
        SummarizeFhirR4ValueSetScopeRequest request,
        CancellationToken cancellationToken = default
    );
    Task<Parameters> TranslateFhirR4ConceptMapAsync(
        TranslateFhirR4ConceptMapRequest request,
        CancellationToken cancellationToken = default
    );
}

public sealed class TerminologyApi : ITerminologyApi
{
    private readonly OrchestrateHttpClient _http;

    internal TerminologyApi(OrchestrateHttpClient http)
    {
        _http = http;
    }

    private static string PageRoute(
        string path,
        KeyValuePair<string, string?>[] parameters,
        int? pageNumber,
        int? pageSize
    )
    {
        if ((pageNumber is null) != (pageSize is null))
            throw new ArgumentException("pageNumber and pageSize must be provided together");
        return RouteBuilder.Build(
            path,
            parameters,
            [
                new(
                    "page.num",
                    (pageNumber ?? 0).ToString(System.Globalization.CultureInfo.InvariantCulture)
                ),
                new(
                    "_count",
                    (pageSize ?? 10000).ToString(System.Globalization.CultureInfo.InvariantCulture)
                ),
            ]
        );
    }

    private async Task<Bundle> GetBundlePagesAsync(
        string path,
        KeyValuePair<string, string?>[] parameters,
        int? pageNumber,
        int? pageSize,
        CancellationToken cancellationToken
    )
    {
        var route = PageRoute(path, parameters, pageNumber, pageSize);
        var result = await _http
            .GetJsonAsync<Bundle>(route, cancellationToken)
            .ConfigureAwait(false);
        if (pageNumber is not null)
            return result;

        var next = result.Link.FirstOrDefault(link => link.Relation == "next")?.Url;
        while (!string.IsNullOrEmpty(next))
        {
            cancellationToken.ThrowIfCancellationRequested();
            var resolved = new Uri(new Uri(new Uri("https://relative.invalid"), route), next);
            route =
                resolved.Host == "relative.invalid" ? resolved.PathAndQuery : resolved.AbsoluteUri;
            var page = await _http
                .GetJsonAsync<Bundle>(route, cancellationToken)
                .ConfigureAwait(false);
            result.Entry.AddRange(page.Entry);
            next = page.Link.FirstOrDefault(link => link.Relation == "next")?.Url;
        }
        result.Link.RemoveAll(link =>
            link.Relation is "self" or "next" or "prev" or "previous" or "first" or "last"
        );
        return result;
    }

    private async Task<CodeSystem> GetCodeSystemPagesAsync(
        string path,
        KeyValuePair<string, string?>[] parameters,
        int? pageNumber,
        int? pageSize,
        CancellationToken cancellationToken
    )
    {
        var result = await _http
            .GetJsonAsync<CodeSystem>(
                PageRoute(path, parameters, pageNumber, pageSize),
                cancellationToken
            )
            .ConfigureAwait(false);
        if (pageNumber is not null)
            return result;

        var page = result;
        var currentPage = 0;
        while (
            page.Concept.Count > 0 && (result.Count is null || result.Concept.Count < result.Count)
        )
        {
            cancellationToken.ThrowIfCancellationRequested();
            currentPage++;
            page = await _http
                .GetJsonAsync<CodeSystem>(
                    PageRoute(path, parameters, currentPage, 10000),
                    cancellationToken
                )
                .ConfigureAwait(false);
            result.Concept.AddRange(page.Concept);
        }
        return result;
    }

    public Task<ClassifyConditionResponse> ClassifyConditionAsync(
        ClassifyConditionRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<ClassifyConditionResponse>(
            "/terminology/v1/classify/condition",
            request,
            cancellationToken
        );

    public Task<IReadOnlyList<ClassifyConditionResponse>> ClassifyConditionAsync(
        IReadOnlyList<ClassifyConditionRequest> request,
        CancellationToken cancellationToken = default
    ) =>
        PostBatchAsync<ClassifyConditionRequest, ClassifyConditionResponse>(
            "/terminology/v1/classify/condition",
            request,
            cancellationToken
        );

    public Task<ClassifyMedicationResponse> ClassifyMedicationAsync(
        ClassifyMedicationRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<ClassifyMedicationResponse>(
            "/terminology/v1/classify/medication",
            request,
            cancellationToken
        );

    public Task<IReadOnlyList<ClassifyMedicationResponse>> ClassifyMedicationAsync(
        IReadOnlyList<ClassifyMedicationRequest> request,
        CancellationToken cancellationToken = default
    ) =>
        PostBatchAsync<ClassifyMedicationRequest, ClassifyMedicationResponse>(
            "/terminology/v1/classify/medication",
            request,
            cancellationToken
        );

    public Task<ClassifyObservationResponse> ClassifyObservationAsync(
        ClassifyObservationRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<ClassifyObservationResponse>(
            "/terminology/v1/classify/observation",
            request,
            cancellationToken
        );

    public Task<IReadOnlyList<ClassifyObservationResponse>> ClassifyObservationAsync(
        IReadOnlyList<ClassifyObservationRequest> request,
        CancellationToken cancellationToken = default
    ) =>
        PostBatchAsync<ClassifyObservationRequest, ClassifyObservationResponse>(
            "/terminology/v1/classify/observation",
            request,
            cancellationToken
        );

    public Task<StandardizeResponse> StandardizeConditionAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<StandardizeResponse>(
            "/terminology/v1/standardize/condition",
            request,
            cancellationToken
        );

    public Task<IReadOnlyList<StandardizeResponse>> StandardizeConditionAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    ) =>
        PostBatchAsync<StandardizeRequest, StandardizeResponse>(
            "/terminology/v1/standardize/condition",
            request,
            cancellationToken
        );

    public Task<StandardizeResponse> StandardizeMedicationAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<StandardizeResponse>(
            "/terminology/v1/standardize/medication",
            request,
            cancellationToken
        );

    public Task<IReadOnlyList<StandardizeResponse>> StandardizeMedicationAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    ) =>
        PostBatchAsync<StandardizeRequest, StandardizeResponse>(
            "/terminology/v1/standardize/medication",
            request,
            cancellationToken
        );

    public Task<StandardizeResponse> StandardizeObservationAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<StandardizeResponse>(
            "/terminology/v1/standardize/observation",
            request,
            cancellationToken
        );

    public Task<IReadOnlyList<StandardizeResponse>> StandardizeObservationAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    ) =>
        PostBatchAsync<StandardizeRequest, StandardizeResponse>(
            "/terminology/v1/standardize/observation",
            request,
            cancellationToken
        );

    public Task<StandardizeResponse> StandardizeProcedureAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<StandardizeResponse>(
            "/terminology/v1/standardize/procedure",
            request,
            cancellationToken
        );

    public Task<IReadOnlyList<StandardizeResponse>> StandardizeProcedureAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    ) =>
        PostBatchAsync<StandardizeRequest, StandardizeResponse>(
            "/terminology/v1/standardize/procedure",
            request,
            cancellationToken
        );

    public Task<StandardizeResponse> StandardizeLabAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<StandardizeResponse>(
            "/terminology/v1/standardize/lab",
            request,
            cancellationToken
        );

    public Task<IReadOnlyList<StandardizeResponse>> StandardizeLabAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    ) =>
        PostBatchAsync<StandardizeRequest, StandardizeResponse>(
            "/terminology/v1/standardize/lab",
            request,
            cancellationToken
        );

    public Task<StandardizeResponse> StandardizeRadiologyAsync(
        StandardizeRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<StandardizeResponse>(
            "/terminology/v1/standardize/radiology",
            request,
            cancellationToken
        );

    public Task<IReadOnlyList<StandardizeResponse>> StandardizeRadiologyAsync(
        IReadOnlyList<StandardizeRequest> request,
        CancellationToken cancellationToken = default
    ) =>
        PostBatchAsync<StandardizeRequest, StandardizeResponse>(
            "/terminology/v1/standardize/radiology",
            request,
            cancellationToken
        );

    public Task<Bundle> StandardizeBundleAsync(
        Bundle bundle,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<Bundle>(
            "/terminology/v1/standardize/fhir/r4",
            bundle,
            cancellationToken
        );

    public Task<CodeSystem> GetFhirR4CodeSystemAsync(
        GetFhirR4CodeSystemRequest request,
        CancellationToken cancellationToken = default
    )
    {
        return GetCodeSystemPagesAsync(
            $"/terminology/v1/fhir/r4/codesystem/{RouteBuilder.Escape(request.CodeSystem)}",
            [new("concept:contains", request.ConceptContains)],
            request.PageNumber,
            request.PageSize,
            cancellationToken
        );
    }

    public Task<Bundle> SummarizeFhirR4CodeSystemsAsync(
        CancellationToken cancellationToken = default
    ) =>
        GetBundlePagesAsync(
            "/terminology/v1/fhir/r4/codesystem",
            [new("_summary", "true")],
            null,
            null,
            cancellationToken
        );

    public Task<Bundle> GetFhirR4ConceptMapsAsync(CancellationToken cancellationToken = default) =>
        GetBundlePagesAsync(
            "/terminology/v1/fhir/r4/conceptmap",
            [],
            null,
            null,
            cancellationToken
        );

    public Task<Parameters> TranslateFhirR4ConceptMapAsync(
        TranslateFhirR4ConceptMapRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<Parameters>(
            "/terminology/v1/fhir/r4/conceptmap/$translate",
            TranslateFhirR4ConceptMapParametersBuilder.Build(request),
            cancellationToken
        );

    public Task<Bundle> SummarizeFhirR4ValueSetScopeAsync(
        SummarizeFhirR4ValueSetScopeRequest request,
        CancellationToken cancellationToken = default
    )
    {
        return GetBundlePagesAsync(
            "/terminology/v1/fhir/r4/valueset",
            [new("extension.scope", request.Scope), new("_summary", "true")],
            null,
            null,
            cancellationToken
        );
    }

    public Task<ValueSet> SummarizeFhirR4ValueSetAsync(
        SummarizeFhirR4ValueSetRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.GetJsonAsync<ValueSet>(
            $"/terminology/v1/fhir/r4/valueset/{RouteBuilder.Escape(request.Id)}?_summary=true",
            cancellationToken
        );

    public Task<ValueSet> GetFhirR4ValueSetAsync(
        GetFhirR4ValueSetRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.GetJsonAsync<ValueSet>(
            $"/terminology/v1/fhir/r4/valueset/{RouteBuilder.Escape(request.Id)}",
            cancellationToken
        );

    public Task<Bundle> GetFhirR4ValueSetsByScopeAsync(
        GetFhirR4ValueSetsByScopeRequest request,
        CancellationToken cancellationToken = default
    )
    {
        return GetBundlePagesAsync(
            "/terminology/v1/fhir/r4/valueset",
            [new("name", request.Name), new("extension.scope", request.Scope)],
            request.PageNumber,
            request.PageSize,
            cancellationToken
        );
    }

    public Task<ValueSet> GetFhirR4ValueSetScopesAsync(
        CancellationToken cancellationToken = default
    ) =>
        _http.GetJsonAsync<ValueSet>(
            "/terminology/v1/fhir/r4/valueset/Rosetta.ValueSetScopes",
            cancellationToken
        );

    public Task<Parameters> GetAllFhirR4ValueSetsForCodesAsync(
        Parameters request,
        CancellationToken cancellationToken = default
    ) =>
        _http.PostJsonAsync<Parameters>(
            "/terminology/v1/fhir/r4/valueset/$classify",
            request,
            cancellationToken
        );

    public Task<CodeSystem> SummarizeFhirR4CodeSystemAsync(
        SummarizeFhirR4CodeSystemRequest request,
        CancellationToken cancellationToken = default
    ) =>
        _http.GetJsonAsync<CodeSystem>(
            $"/terminology/v1/fhir/r4/codesystem/{RouteBuilder.Escape(request.CodeSystem)}?_summary=true",
            cancellationToken
        );

    private async Task<IReadOnlyList<TOut>> PostBatchAsync<TIn, TOut>(
        string route,
        IReadOnlyList<TIn> request,
        CancellationToken cancellationToken
    )
    {
        var response = await _http
            .PostJsonAsync<BatchResponse<TOut>>(
                $"{route}/batch",
                new BatchRequest<TIn> { Items = request },
                cancellationToken
            )
            .ConfigureAwait(false);
        return response.Items;
    }
}
