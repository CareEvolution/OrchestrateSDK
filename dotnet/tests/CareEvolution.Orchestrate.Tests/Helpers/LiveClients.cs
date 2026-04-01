namespace CareEvolution.Orchestrate.Tests.Helpers;

internal static class LiveClients
{
    public static OrchestrateApi CreateOrchestrateApi(HttpClient httpClient) => new(httpClient);

    public static IdentityApi CreateIdentityApi(HttpClient httpClient) => new(httpClient);

    public static LocalHashingApi CreateLocalHashingApi(HttpClient httpClient) => new(httpClient);
}
