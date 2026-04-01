using System.Net;
using Hl7.Fhir.Model;

namespace CareEvolution.Orchestrate.Exceptions;

/// <summary>
/// Raised when the Orchestrate API returns a 4xx or 5xx status code.
/// </summary>
public sealed class OrchestrateClientException(
    string responseText,
    IReadOnlyList<string> issues,
    HttpStatusCode statusCode,
    OperationOutcome? operationOutcome = null
)
    : OrchestrateHttpException(
        issues.Count > 0 ? $"\n  * {string.Join(" \n  * ", issues)}" : responseText,
        statusCode
    )
{
    public string ResponseText { get; } = responseText;

    public IReadOnlyList<string> Issues { get; } = issues;

    public OperationOutcome? OperationOutcome { get; } = operationOutcome;
}
