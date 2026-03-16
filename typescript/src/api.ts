import { ConvertApi } from "./convert.js";
import { IHttpHandler } from "./httpHandler.js";
import { createHttpHandler } from "./httpHandlerFactory.js";
import { InsightApi } from "./insight.js";
import { TerminologyApi } from "./terminology.js";

export interface Configuration {
  apiKey?: string;
  timeoutMs?: number;
}

/**
 * Entry point for the Orchestrate Terminology, Convert, and Insight APIs.
 *
 * Configuration can be supplied through the constructor or environment
 * variables. Constructor values take precedence over environment variables.
 * For this client, `apiKey` overrides `ORCHESTRATE_API_KEY`, `timeoutMs`
 * overrides `ORCHESTRATE_TIMEOUT_MS`, and `ORCHESTRATE_BASE_URL` can be used
 * to override the default base URL of `https://api.careevolutionapi.com`.
 *
 * `ORCHESTRATE_ADDITIONAL_HEADERS` can be used to add headers to every
 * request. The value must be a JSON object. These headers are merged in before
 * the SDK's standard `Accept`, `Content-Type`, and authentication headers are
 * applied, so SDK-managed headers take precedence on conflicts.
 */
export class OrchestrateApi {
  readonly terminology: TerminologyApi;
  readonly convert: ConvertApi;
  readonly insight: InsightApi;

  /**
   * Exposes the underlying IHttpHandler instance for advanced usage. This is
   * made available to take advantage of features not yet wrapped in
   * OrchestrateApi. This may change without warning.
   * @deprecated Not a stable API.
   */
  readonly httpHandler: IHttpHandler;

  /**
   * Creates a configured Orchestrate API client.
   *
   * `apiKey` is sent as the `x-api-key` header. If it is omitted, the client
   * uses `ORCHESTRATE_API_KEY` when it is set.
   *
   * `timeoutMs` is the request timeout in milliseconds. If it is omitted, the
   * client uses `ORCHESTRATE_TIMEOUT_MS` when it is set, otherwise it defaults
   * to `120000`.
   *
   * `ORCHESTRATE_BASE_URL` can be used to override the default API base URL
   * without changing application code.
   */
  constructor(configuration: Configuration | undefined = {}) {
    const httpHandler = createHttpHandler(configuration.apiKey, undefined, configuration.timeoutMs);

    this.terminology = new TerminologyApi(httpHandler);
    this.convert = new ConvertApi(httpHandler);
    this.insight = new InsightApi(httpHandler);

    this.httpHandler = httpHandler;
  }
}
