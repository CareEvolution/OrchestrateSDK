using System.Net;

namespace CareEvolution.Orchestrate.Exceptions;

public sealed class OrchestrateClientError(
    string responseText,
    IReadOnlyList<string> issues,
    HttpStatusCode statusCode
)
    : OrchestrateHttpError(
        issues.Count > 0 ? $"\n  * {string.Join(" \n  * ", issues)}" : responseText,
        statusCode
    )
{
    public string ResponseText { get; } = responseText;

    public IReadOnlyList<string> Issues { get; } = issues;
}
