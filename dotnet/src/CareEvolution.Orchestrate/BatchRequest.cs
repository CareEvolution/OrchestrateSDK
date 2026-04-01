namespace CareEvolution.Orchestrate;

internal sealed class BatchRequest<T>
{
    public required IReadOnlyList<T> Items { get; init; }
}
