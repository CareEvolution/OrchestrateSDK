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
    Task<Bundle> GetFhirR4ConceptMapsAsync(
        CancellationToken cancellationToken = default,
        int? pageNumber = null,
        int? pageSize = null
    );
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
    Task<Bundle> SummarizeFhirR4CodeSystemsAsync(
        CancellationToken cancellationToken = default,
        int? pageNumber = null,
        int? pageSize = null
    );
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

    private async Task<T> GetPagesAsync<T, TItem>(
        string path,
        KeyValuePair<string, string?>[] parameters,
        int? pageNumber,
        int? pageSize,
        Func<T, List<TItem>> items,
        CancellationToken cancellationToken
    )
    {
        if ((pageNumber is null) != (pageSize is null))
        {
            throw new ArgumentException("pageNumber and pageSize must be provided together");
        }
        var automatic = pageNumber is null && pageSize is null;
        if (automatic)
        {
            pageNumber = 0;
            pageSize = 10000;
        }

        Task<T> FetchPage() =>
            _http.GetJsonAsync<T>(
                RouteBuilder.Build(
                    path,
                    parameters,
                    [
                        new(
                            "page.num",
                            pageNumber?.ToString(System.Globalization.CultureInfo.InvariantCulture)
                        ),
                        new(
                            "_count",
                            pageSize?.ToString(System.Globalization.CultureInfo.InvariantCulture)
                        ),
                    ]
                ),
                cancellationToken
            );

        var result = await FetchPage().ConfigureAwait(false);
        if (!automatic)
            return result;

        var total = result switch
        {
            Bundle bundle => bundle.Total,
            CodeSystem codeSystem => codeSystem.Count,
            _ => null,
        };
        var page = result;
        while (items(page).Count > 0 && (total is null || items(result).Count < total))
        {
            cancellationToken.ThrowIfCancellationRequested();
            pageNumber++;
            page = await FetchPage().ConfigureAwait(false);
            items(result).AddRange(items(page));
        }
        if (result is Bundle aggregatedBundle)
        {
            aggregatedBundle.Link.RemoveAll(link =>
                link.Relation is "self" or "next" or "prev" or "previous" or "first" or "last"
            );
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
        return GetPagesAsync(
            $"/terminology/v1/fhir/r4/codesystem/{RouteBuilder.Escape(request.CodeSystem)}",
            [new("concept:contains", request.ConceptContains)],
            request.PageNumber,
            request.PageSize,
            (CodeSystem resource) => resource.Concept,
            cancellationToken
        );
    }

    public Task<Bundle> SummarizeFhirR4CodeSystemsAsync(
        CancellationToken cancellationToken = default,
        int? pageNumber = null,
        int? pageSize = null
    ) =>
        GetPagesAsync(
            "/terminology/v1/fhir/r4/codesystem",
            [new("_summary", "true")],
            pageNumber,
            pageSize,
            (Bundle resource) => resource.Entry,
            cancellationToken
        );

    public Task<Bundle> GetFhirR4ConceptMapsAsync(
        CancellationToken cancellationToken = default,
        int? pageNumber = null,
        int? pageSize = null
    ) =>
        GetPagesAsync(
            "/terminology/v1/fhir/r4/conceptmap",
            [],
            pageNumber,
            pageSize,
            (Bundle resource) => resource.Entry,
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
        return GetPagesAsync(
            "/terminology/v1/fhir/r4/valueset",
            [new("extension.scope", request.Scope), new("_summary", "true")],
            request.PageNumber,
            request.PageSize,
            (Bundle resource) => resource.Entry,
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
        return GetPagesAsync(
            "/terminology/v1/fhir/r4/valueset",
            [new("name", request.Name), new("extension.scope", request.Scope)],
            request.PageNumber,
            request.PageSize,
            (Bundle resource) => resource.Entry,
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
