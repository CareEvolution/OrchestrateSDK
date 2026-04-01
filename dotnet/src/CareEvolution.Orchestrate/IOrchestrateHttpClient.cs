using System.ComponentModel;

namespace CareEvolution.Orchestrate;

[EditorBrowsable(EditorBrowsableState.Advanced)]
public interface IOrchestrateHttpClient
{
    HttpClient HttpClient { get; }

    Task<T> SendAsync<T>(
        HttpMethod method,
        string path,
        HttpContent? content = null,
        string accept = "application/json",
        CancellationToken cancellationToken = default
    );

    Task<T> GetJsonAsync<T>(string path, CancellationToken cancellationToken = default);

    Task<T> PostJsonAsync<T>(
        string path,
        object? body,
        CancellationToken cancellationToken = default
    );
}
