using System.ComponentModel;

namespace CareEvolution.Orchestrate;

public interface IOrchestrateApi
{
    ITerminologyApi Terminology { get; }
    IConvertApi Convert { get; }
    IInsightApi Insight { get; }
    IOrchestrateHttpClient HttpHandler { get; }
}

public sealed class OrchestrateApi : IOrchestrateApi
{
    private readonly OrchestrateHttpClient _http;

    public OrchestrateApi(HttpClient httpClient, OrchestrateClientOptions? options = null)
    {
        _http = new OrchestrateHttpClient(EnvironmentConfiguration.Resolve(options), httpClient);
        Terminology = new TerminologyApi(_http);
        Convert = new ConvertApi(_http);
        Insight = new InsightApi(_http);
    }

    public ITerminologyApi Terminology { get; }

    public IConvertApi Convert { get; }

    public IInsightApi Insight { get; }

    [EditorBrowsable(EditorBrowsableState.Advanced)]
    public IOrchestrateHttpClient HttpHandler => _http;
}
