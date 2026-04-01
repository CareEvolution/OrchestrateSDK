using Hl7.Fhir.Rest;

namespace CareEvolution.Orchestrate;

internal static class RouteBuilder
{
    public static string Build(
        string path,
        params IEnumerable<KeyValuePair<string, string?>>[] querySets
    )
    {
        var query = BuildQuery(querySets.SelectMany(static set => set));
        return string.IsNullOrWhiteSpace(query) ? path : $"{path}?{query}";
    }

    public static string BuildQuery(IEnumerable<KeyValuePair<string, string?>> values)
    {
        var segments = values
            .Where(static pair => !string.IsNullOrWhiteSpace(pair.Value))
            .Select(static pair =>
                $"{Uri.EscapeDataString(pair.Key)}={Uri.EscapeDataString(pair.Value!)}"
            )
            .ToArray();

        return string.Join("&", segments);
    }

    public static string Escape(string value) => Uri.EscapeDataString(value);
}
