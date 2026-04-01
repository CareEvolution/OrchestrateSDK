namespace CareEvolution.Orchestrate.Exceptions;

/// <summary>
/// Base class for all Orchestrate exceptions.
/// </summary>
public class OrchestrateException(string message) : Exception(message) { }
