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
        var route = RouteBuilder.Build(
            $"/terminology/v1/fhir/r4/codesystem/{request.CodeSystem}",
            [
                new KeyValuePair<string, string?>("page.num", request.PageNumber?.ToString()),
                new KeyValuePair<string, string?>("_count", request.PageSize?.ToString()),
                new KeyValuePair<string, string?>("concept:contains", request.ConceptContains),
            ]
        );
        return _http.GetJsonAsync<CodeSystem>(route, cancellationToken);
    }

    public Task<Bundle> SummarizeFhirR4CodeSystemsAsync(
        CancellationToken cancellationToken = default
    ) =>
        _http.GetJsonAsync<Bundle>(
            "/terminology/v1/fhir/r4/codesystem?_summary=true",
            cancellationToken
        );

    public Task<Bundle> GetFhirR4ConceptMapsAsync(CancellationToken cancellationToken = default) =>
        _http.GetJsonAsync<Bundle>("/terminology/v1/fhir/r4/conceptmap", cancellationToken);

    public Task<Parameters> TranslateFhirR4ConceptMapAsync(
        TranslateFhirR4ConceptMapRequest request,
        CancellationToken cancellationToken = default
    )
    {
        var route = RouteBuilder.Build(
            "/terminology/v1/fhir/r4/conceptmap/$translate",
            [
                new KeyValuePair<string, string?>("code", request.Code),
                new KeyValuePair<string, string?>("domain", request.Domain),
            ]
        );
        return _http.GetJsonAsync<Parameters>(route, cancellationToken);
    }

    public Task<Bundle> SummarizeFhirR4ValueSetScopeAsync(
        SummarizeFhirR4ValueSetScopeRequest request,
        CancellationToken cancellationToken = default
    )
    {
        var route = RouteBuilder.Build(
            "/terminology/v1/fhir/r4/valueset",
            [
                new KeyValuePair<string, string?>("extension.scope", request.Scope),
                new KeyValuePair<string, string?>("_summary", "true"),
            ]
        );
        return _http.GetJsonAsync<Bundle>(route, cancellationToken);
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
        var route = RouteBuilder.Build(
            "/terminology/v1/fhir/r4/valueset",
            [
                new KeyValuePair<string, string?>("name", request.Name),
                new KeyValuePair<string, string?>("page.num", request.PageNumber?.ToString()),
                new KeyValuePair<string, string?>("_count", request.PageSize?.ToString()),
                new KeyValuePair<string, string?>("extension.scope", request.Scope),
            ]
        );
        return _http.GetJsonAsync<Bundle>(route, cancellationToken);
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
