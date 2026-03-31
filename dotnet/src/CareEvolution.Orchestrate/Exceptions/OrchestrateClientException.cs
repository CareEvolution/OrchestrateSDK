using System.Net;

namespace CareEvolution.Orchestrate.Exceptions;

/// <summary>
/// Raised when the Orchestrate API returns a 4xx or 5xx status code.
/// </summary>
public sealed class OrchestrateClientException(
    string responseText,
    IReadOnlyList<string> issues,
    HttpStatusCode statusCode
)
    : OrchestrateHttpException(
        issues.Count > 0 ? $"\n  * {string.Join(" \n  * ", issues)}" : responseText,
        statusCode
    )
{
    public string ResponseText { get; } = responseText;

    public IReadOnlyList<string> Issues { get; } = issues;
}
