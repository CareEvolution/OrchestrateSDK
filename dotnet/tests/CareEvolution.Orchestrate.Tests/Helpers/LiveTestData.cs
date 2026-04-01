using System.Text.Json;
using System.Text.Json.Nodes;
using Hl7.Fhir.Serialization;

namespace CareEvolution.Orchestrate.Tests.Helpers;

internal static class LiveTestData
{
    private static readonly string BasePath = Path.Combine(AppContext.BaseDirectory, "LiveData");
    private static readonly FhirJsonFastParser FhirParser = new(
        new ParserSettings(global::Hl7.Fhir.Model.Version.R4)
        {
            AllowUnrecognizedEnums = true,
            AcceptUnknownMembers = true,
            PermissiveParsing = true,
        }
    );

    public static string Cda => ReadText("cda.xml");

    public static string EncodingCda => ReadText("encoding_cda.xml");

    public static string Hl7 => ReadText("hl7.txt");

    public static Bundle R4Bundle => ReadBundle("r4_bundle.json");

    public static Bundle RiskProfileBundle => ReadBundle("risk_profile_bundle.json");

    public static string X12Document => ReadText("x12.txt");

    public static JsonNode Dstu2Bundle => ReadJsonNode("dstu2_bundle.json");

    public static JsonNode Stu3Bundle => ReadJsonNode("stu3_bundle.json");

    public static Bundle NemsisBundle => ReadBundle("nemsis_bundle.json");

    public static string BlindedDemographicData =>
        "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";

    private static string ReadText(string fileName) =>
        File.ReadAllText(Path.Combine(BasePath, fileName));

    private static Bundle ReadBundle(string fileName) =>
        (Bundle)FhirParser.Parse(ReadText(fileName), typeof(Bundle));

    private static JsonNode ReadJsonNode(string fileName) =>
        JsonNode.Parse(ReadText(fileName))
        ?? throw new InvalidOperationException($"Unable to deserialize JSON fixture '{fileName}'.");
}
