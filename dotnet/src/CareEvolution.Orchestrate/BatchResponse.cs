namespace CareEvolution.Orchestrate;

internal sealed class BatchResponse<T>
{
    public required List<T> Items { get; init; }
}
