using System.ComponentModel;

namespace CareEvolution.Orchestrate.Identity;

public sealed class LocalHashingApi : IDisposable
{
    private readonly OrchestrateHttpClient _http;

    public LocalHashingApi(LocalHashingApiOptions? options = null)
        : this(httpClient: null, options) { }

    public LocalHashingApi(HttpClient? httpClient, LocalHashingApiOptions? options = null)
    {
        _http = new OrchestrateHttpClient(EnvironmentConfiguration.Resolve(options), httpClient);
    }

    [EditorBrowsable(EditorBrowsableState.Advanced)]
    public IOrchestrateHttpClient Transport => _http;

    public HttpClient HttpClient => _http.HttpClient;

    public Task<HashDemographicResponse> HashAsync(
        Demographic demographic,
        CancellationToken cancellationToken = default
    ) => _http.PostJsonAsync<HashDemographicResponse>("/hash", demographic, cancellationToken);

    public void Dispose() => _http.Dispose();
}
