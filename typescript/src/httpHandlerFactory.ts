import { HttpHandler, IHttpHandler } from "./httpHandler.js";

const baseUrlEnvironmentVariable = "ORCHESTRATE_BASE_URL";
const identityUrlEnvironmentVariable = "ORCHESTRATE_IDENTITY_URL";
const identityLocalHashingUrlEnvironmentVariable = "ORCHESTRATE_IDENTITY_LOCAL_HASHING_URL";
const additionalHeadersEnvironmentVariable = "ORCHESTRATE_ADDITIONAL_HEADERS";
const apiKeyEnvironmentVariable = "ORCHESTRATE_API_KEY";
const identityApiKeyEnvironmentVariable = "ORCHESTRATE_IDENTITY_API_KEY";
const identityMetricsKeyEnvironmentVariable = "ORCHESTRATE_IDENTITY_METRICS_KEY";

function getPriorityFromEnvironment(argument: string | undefined, environmentVariable: string): string | undefined {
  return argument || process.env[environmentVariable];
}

function getPriorityBaseUrl(baseUrl: string | undefined): string {
  return getPriorityFromEnvironment(baseUrl, baseUrlEnvironmentVariable) || "https://api.careevolutionapi.com";
}

function getAdditionalHeaders(): { [key: string]: string; } | undefined {
  if (process.env[additionalHeadersEnvironmentVariable]) {
    return JSON.parse(process.env[additionalHeadersEnvironmentVariable]);
  }
  return undefined;
}

export function createHttpHandler(
  apiKey: string | undefined,
  baseUrl: string | undefined = undefined
): IHttpHandler {
  const additionalHeaders = getAdditionalHeaders();
  const priorityBaseUrl = getPriorityBaseUrl(baseUrl);
  const defaultHeaders = {
    ...additionalHeaders,
    "Content-Type": "application/json",
    Accept: "application/json",
  } as { [key: string]: string; };

  const priorityApiKey = getPriorityFromEnvironment(apiKey, apiKeyEnvironmentVariable);

  if (priorityApiKey) {
    defaultHeaders["x-api-key"] = priorityApiKey;
  }

  return new HttpHandler(priorityBaseUrl, defaultHeaders);
}

export function createIdentityHttpHandler(
  apiKey: string | undefined,
  metricsKey: string | undefined,
  baseUrl: string | undefined
): IHttpHandler {
  const additionalHeaders = getAdditionalHeaders();
  const priorityUrl = getPriorityFromEnvironment(baseUrl, identityUrlEnvironmentVariable);
  const defaultHeaders = {
    ...additionalHeaders,
    "Content-Type": "application/json",
    Accept: "application/json",
  } as { [key: string]: string; };

  const priorityApiKey = getPriorityFromEnvironment(apiKey, identityApiKeyEnvironmentVariable);
  const priorityMetricsKey = getPriorityFromEnvironment(metricsKey, identityMetricsKeyEnvironmentVariable);

  if (!priorityUrl) {
    throw new Error(`Identity URL is required. Specify in the constructor or set '${identityUrlEnvironmentVariable}' environment variable.`);
  }

  if (priorityApiKey) {
    defaultHeaders["x-api-key"] = priorityApiKey;
  }
  if (priorityMetricsKey) {
    const headerMetricsKey = priorityMetricsKey.replace("Basic ", "");
    defaultHeaders["Authorization"] = `Basic ${headerMetricsKey}`;
  }

  return new HttpHandler(priorityUrl, defaultHeaders);
}

export function createLocalHashingHttpHandler(
  baseUrl: string | undefined
): IHttpHandler {
  const additionalHeaders = getAdditionalHeaders();
  const priorityUrl = getPriorityFromEnvironment(baseUrl, identityLocalHashingUrlEnvironmentVariable);
  const defaultHeaders = {
    ...additionalHeaders,
    "Content-Type": "application/json",
    Accept: "application/json",
  } as { [key: string]: string; };

  if (!priorityUrl) {
    throw new Error(`Local hashing URL is required. Specify in the constructor or set '${identityLocalHashingUrlEnvironmentVariable}' environment variable.`);
  }

  return new HttpHandler(priorityUrl, defaultHeaders);
}