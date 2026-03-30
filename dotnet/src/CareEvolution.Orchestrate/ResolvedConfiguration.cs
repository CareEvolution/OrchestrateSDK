namespace CareEvolution.Orchestrate;

internal sealed record ResolvedConfiguration(
    string BaseUrl,
    int TimeoutMs,
    IReadOnlyDictionary<string, string> AdditionalHeaders,
    string? ApiKey = null,
    string? Authorization = null
);
