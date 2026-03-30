namespace CareEvolution.Orchestrate.Tests.Helpers;

internal static class LiveClients
{
    public static OrchestrateApi CreateOrchestrateApi() => new();

    public static IdentityApi CreateIdentityApi() => new();

    public static LocalHashingApi CreateLocalHashingApi() => new();
}
