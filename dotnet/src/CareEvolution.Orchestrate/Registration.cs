using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Options;

namespace CareEvolution.Orchestrate;

public static class Registration
{
    public static IServiceCollection AddOrchestrateApi(this IServiceCollection services) =>
        services.AddOrchestrateApi(configure: null);

    public static IServiceCollection AddOrchestrateApi(
        this IServiceCollection services,
        Action<OrchestrateClientOptions>? configure
    )
    {
        services.AddOptions<OrchestrateClientOptions>();

        if (configure is not null)
        {
            services.Configure(configure);
        }

        services.AddHttpClient(nameof(OrchestrateApi));
        services.AddTransient<IOrchestrateApi>(serviceProvider => new OrchestrateApi(
            serviceProvider
                .GetRequiredService<IHttpClientFactory>()
                .CreateClient(nameof(OrchestrateApi)),
            serviceProvider.GetRequiredService<IOptions<OrchestrateClientOptions>>().Value
        ));

        return services;
    }
}
