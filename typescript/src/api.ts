import { ConvertApi } from "./convert";
import { HttpHandler } from "./httpHandler";
import { InsightApi } from "./insight";
import { TerminologyApi } from "./terminology";

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
