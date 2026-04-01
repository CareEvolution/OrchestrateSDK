using System.Net.Sockets;

namespace CareEvolution.Orchestrate.Tests.Helpers;

internal static class LiveTestEnvironment
{
    private static readonly object SyncRoot = new();
    private static bool _loaded;

    public const string OrchestrateApiKey = "ORCHESTRATE_API_KEY";
    public const string IdentityApiKey = "ORCHESTRATE_IDENTITY_API_KEY";
    public const string IdentityMetricsKey = "ORCHESTRATE_IDENTITY_METRICS_KEY";
    public const string IdentityUrl = "ORCHESTRATE_IDENTITY_URL";
    public const string LocalHashingUrl = "ORCHESTRATE_IDENTITY_LOCAL_HASHING_URL";

    public static string? GetSkipReason(params string[] requiredVariables)
    {
        EnsureEnvironmentLoaded();

        var missingVariables = requiredVariables
            .Where(variable =>
                string.IsNullOrWhiteSpace(Environment.GetEnvironmentVariable(variable))
            )
            .ToArray();

        if (missingVariables.Length == 0)
        {
            return GetUnavailableServiceReason(requiredVariables);
        }

        return $"Live test requires environment variables: {string.Join(", ", missingVariables)}";
    }

    private static string? GetUnavailableServiceReason(IEnumerable<string> requiredVariables)
    {
        foreach (var variable in requiredVariables)
        {
            if (variable is not (IdentityUrl or LocalHashingUrl))
            {
                continue;
            }

            var rawUrl = Environment.GetEnvironmentVariable(variable);
            if (
                string.IsNullOrWhiteSpace(rawUrl)
                || !Uri.TryCreate(rawUrl, UriKind.Absolute, out var uri)
            )
            {
                continue;
            }

            if (!IsLocalHost(uri.Host))
            {
                continue;
            }

            var port = uri.IsDefaultPort
                ? uri.Scheme.Equals("https", StringComparison.OrdinalIgnoreCase)
                    ? 443
                    : 80
                : uri.Port;

            if (!CanConnect(uri.Host, port))
            {
                return $"Live test requires {variable} service at {uri.Host}:{port} to be running.";
            }
        }

        return null;
    }

    private static bool IsLocalHost(string host) =>
        host.Equals("localhost", StringComparison.OrdinalIgnoreCase)
        || host.Equals("127.0.0.1", StringComparison.OrdinalIgnoreCase)
        || host.Equals("::1", StringComparison.OrdinalIgnoreCase);

    private static bool CanConnect(string host, int port)
    {
        try
        {
            using var client = new TcpClient();
            var connectTask = client.ConnectAsync(host, port);
            return connectTask.Wait(TimeSpan.FromMilliseconds(250)) && client.Connected;
        }
        catch
        {
            return false;
        }
    }

    private static void EnsureEnvironmentLoaded()
    {
        if (_loaded)
        {
            return;
        }

        lock (SyncRoot)
        {
            if (_loaded)
            {
                return;
            }

            var current = new DirectoryInfo(AppContext.BaseDirectory);
            while (current is not null)
            {
                var envPath = Path.Combine(current.FullName, ".env");
                if (File.Exists(envPath))
                {
                    LoadDotEnv(envPath);
                    break;
                }

                current = current.Parent;
            }

            _loaded = true;
        }
    }

    private static void LoadDotEnv(string path)
    {
        foreach (var rawLine in File.ReadAllLines(path))
        {
            var line = rawLine.Trim();
            if (string.IsNullOrWhiteSpace(line) || line.StartsWith('#'))
            {
                continue;
            }

            var separatorIndex = line.IndexOf('=');
            if (separatorIndex <= 0)
            {
                continue;
            }

            var key = line[..separatorIndex].Trim();
            var value = line[(separatorIndex + 1)..].Trim();
            if (
                value.Length >= 2
                && (
                    (value.StartsWith('"') && value.EndsWith('"'))
                    || (value.StartsWith('\'') && value.EndsWith('\''))
                )
            )
            {
                value = value[1..^1];
            }

            Environment.SetEnvironmentVariable(key, value);
        }
    }
}

public sealed class LiveFactAttribute : FactAttribute
{
    public LiveFactAttribute(params string[] requiredVariables)
    {
        Skip = LiveTestEnvironment.GetSkipReason(requiredVariables);
    }
}

public sealed class LiveTheoryAttribute : TheoryAttribute
{
    public LiveTheoryAttribute(params string[] requiredVariables)
    {
        Skip = LiveTestEnvironment.GetSkipReason(requiredVariables);
    }
}
