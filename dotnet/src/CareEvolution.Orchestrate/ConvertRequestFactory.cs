using System.Text.Json.Serialization;

namespace CareEvolution.Orchestrate;

public static class ConvertRequestFactory
{
    public static ConvertCombineFhirR4BundlesRequest GenerateConvertCombinedFhirBundlesRequestFromBundles(
        IEnumerable<Bundle> fhirBundles,
        string? personId = null
    )
    {
        var content = string.Join("\n", fhirBundles.Select(OrchestrateHttpClient.Serialize));

        return new ConvertCombineFhirR4BundlesRequest { Content = content, PatientId = personId };
    }
}
