using System.Net;

namespace CareEvolution.Orchestrate.Exceptions;

/// <summary>
/// Raised when an HTTP request to the Orchestrate API fails.
/// </summary>
public class OrchestrateHttpException(string message, HttpStatusCode? statusCode = null)
    : OrchestrateException(message)
{
    public HttpStatusCode? StatusCode { get; } = statusCode;
}
