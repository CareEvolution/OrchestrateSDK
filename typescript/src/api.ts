import { ConvertApi } from "./convert.js";
import { HttpHandler } from "./httpHandler.js";
import { InsightApi } from "./insight.js";
import { TerminologyApi } from "./terminology.js";

export interface Configuration {
  apiKey?: string;
  baseUrl?: string;
  additionalHeaders?: { [key: string]: string; };
}


export class OrchestrateApi {
  terminology: TerminologyApi;
  convert: ConvertApi;
  insight: InsightApi;

  constructor(configuration: Configuration) {
    const defaultHeaders = {
      ...configuration.additionalHeaders ?? {},
      ...{
        "Content-Type": "application/json",
        "Accept": "application/json",
      }
    } as { [key: string]: string; };

    if (configuration.apiKey) {
      defaultHeaders["x-api-key"] = configuration.apiKey;
    }

    const httpHandler = new HttpHandler(
      configuration.baseUrl ?? "https://api.careevolutionapi.com",
      defaultHeaders,
    );
    this.terminology = new TerminologyApi(httpHandler);
    this.convert = new ConvertApi(httpHandler);
    this.insight = new InsightApi(httpHandler);
  }
}
