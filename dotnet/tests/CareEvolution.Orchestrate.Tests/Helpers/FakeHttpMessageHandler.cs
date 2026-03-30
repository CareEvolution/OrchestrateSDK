using System.Net;
using System.Text;

namespace CareEvolution.Orchestrate.Tests.Helpers;

internal sealed class FakeHttpMessageHandler : HttpMessageHandler
{
    private readonly Func<
        HttpRequestMessage,
        CancellationToken,
        Task<HttpResponseMessage>
    > _responder;

    public FakeHttpMessageHandler(
        Func<HttpRequestMessage, CancellationToken, Task<HttpResponseMessage>> responder
    )
    {
        _responder = responder;
    }

    public RequestSnapshot? LastRequest { get; private set; }

    protected override async Task<HttpResponseMessage> SendAsync(
        HttpRequestMessage request,
        CancellationToken cancellationToken
    )
    {
        LastRequest = await RequestSnapshot.CreateAsync(request, cancellationToken);
        return await _responder(request, cancellationToken);
    }
}

internal sealed record RequestSnapshot(
    HttpMethod Method,
    Uri? RequestUri,
    IReadOnlyDictionary<string, IReadOnlyList<string>> Headers,
    string? Body
)
{
    public static async Task<RequestSnapshot> CreateAsync(
        HttpRequestMessage request,
        CancellationToken cancellationToken
    )
    {
        var contentHeaders = request.Content is null
            ? Enumerable.Empty<KeyValuePair<string, IEnumerable<string>>>()
            : request.Content.Headers;

        var headers = request
            .Headers.Concat(contentHeaders)
            .ToDictionary(
                pair => pair.Key,
                pair => (IReadOnlyList<string>)pair.Value.ToList(),
                StringComparer.OrdinalIgnoreCase
            );

        var body = request.Content is null
            ? null
            : await request.Content.ReadAsStringAsync(cancellationToken);

        return new RequestSnapshot(request.Method, request.RequestUri, headers, body);
    }
}

internal static class FakeResponses
{
    public static HttpResponseMessage Json(
        string json,
        HttpStatusCode statusCode = HttpStatusCode.OK
    )
    {
        return new HttpResponseMessage(statusCode)
        {
            Content = new StringContent(json, Encoding.UTF8, "application/json"),
        };
    }

    public static HttpResponseMessage Text(
        string text,
        string mediaType,
        HttpStatusCode statusCode = HttpStatusCode.OK
    )
    {
        return new HttpResponseMessage(statusCode)
        {
            Content = new StringContent(text, Encoding.UTF8, mediaType),
        };
    }

    public static HttpResponseMessage Bytes(
        byte[] bytes,
        string mediaType,
        HttpStatusCode statusCode = HttpStatusCode.OK
    )
    {
        return new HttpResponseMessage(statusCode)
        {
            Content = new ByteArrayContent(bytes)
            {
                Headers =
                {
                    ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue(mediaType),
                },
            },
        };
    }
}
