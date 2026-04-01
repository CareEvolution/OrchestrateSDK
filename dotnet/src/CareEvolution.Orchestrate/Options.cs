namespace CareEvolution.Orchestrate;

public class OrchestrateClientOptions
{
    public string? ApiKey { get; set; }

    public string? BaseUrl { get; set; }

    public int? TimeoutMs { get; set; }
}

public class IdentityApiOptions
{
    public string? Url { get; set; }

    public string? ApiKey { get; set; }

    public string? MetricsKey { get; set; }

    public int? TimeoutMs { get; set; }
}

public class LocalHashingApiOptions
{
    public string? Url { get; set; }

    public int? TimeoutMs { get; set; }
}
