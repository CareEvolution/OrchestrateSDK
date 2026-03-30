using System.Net;

namespace CareEvolution.Orchestrate.Exceptions;

public class OrchestrateHttpError(string message, HttpStatusCode? statusCode = null)
    : OrchestrateError(message)
{
    public HttpStatusCode? StatusCode { get; } = statusCode;
}
