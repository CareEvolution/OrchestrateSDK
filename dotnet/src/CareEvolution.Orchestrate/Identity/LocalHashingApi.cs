using System.ComponentModel;

namespace CareEvolution.Orchestrate.Identity;

public sealed class LocalHashingApi(HttpClient httpClient, LocalHashingApiOptions? options = null)
{
    private readonly OrchestrateHttpClient _http = new(
        EnvironmentConfiguration.Resolve(options),
        httpClient
    );

    [EditorBrowsable(EditorBrowsableState.Advanced)]
    public IOrchestrateHttpClient Transport => _http;

    public HttpClient HttpClient => _http.HttpClient;

    public Task<HashDemographicResponse> HashAsync(
        Demographic demographic,
        CancellationToken cancellationToken = default
    ) => _http.PostJsonAsync<HashDemographicResponse>("/hash", demographic, cancellationToken);
}
