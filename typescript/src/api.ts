import {
  ConvertCdaToFhirR4Request,
  ConvertCdaToFhirR4Response,
  ConvertCdaToPdfRequest,
  ConvertCdaToPdfResponse,
  ConvertCombineFhirR4BundlesRequest,
  ConvertCombineFhirR4BundlesResponse,
  ConvertFhirR4ToCdaRequest,
  ConvertFhirR4ToCdaResponse,
  ConvertFhirR4ToOmopRequest,
  ConvertFhirR4ToOmopResponse,
  ConvertHl7ToFhirR4Request,
  ConvertHl7ToFhirR4Response,
} from "./convert";
import { InsightRiskProfileRequest, InsightRiskProfileResponse } from "./insight";
import {
  ClassifyConditionRequest,
  ClassifyConditionResponse,
  ClassifyFhirR4ValueSetMembershipRequest,
  ClassifyFhirR4ValueSetMembershipResponse,
  ClassifyMedicationRequest,
  ClassifyMedicationResponse,
  ClassifyObservationRequest,
  ClassifyObservationResponse,
  GetFhirR4CodeSystemRequest,
  GetFhirR4CodeSystemResponse,
  GetFhirR4ConceptMapResponse,
  GetFhirR4ValueSetRequest,
  GetFhirR4ValueSetResponse,
  GetFhirR4ValueSetScopeRequest,
  GetFhirR4ValueSetScopeResponse,
  GetFhirR4ValueSetScopesResponse,
  StandardizeConditionResponse,
  StandardizeLabResponse,
  StandardizeMedicationResponse,
  StandardizeObservationResponse,
  StandardizeRadiologyResponse,
  StandardizeRequest,
  SummarizeFhirR4CodeSystemRequest,
  SummarizeFhirR4CodeSystemResponse,
  SummarizeFhirR4CodeSystemsResponse,
  SummarizeFhirR4ValueSetRequest,
  SummarizeFhirR4ValueSetResponse,
  SummarizeFhirR4ValueSetScopeRequest,
  SummarizeFhirR4ValueSetScopeResponse,
  TranslateFhirR4ConceptMapRequest,
  TranslateFhirR4ConceptMapResponse,
} from "./terminology";

export interface Configuration {
  apiKey?: string;
  baseUrl?: string;
  additionalHeaders?: { [key: string]: string; };
}

export class OrchestrateApi {
  rosettaApi: RosettaApi;

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

    this.rosettaApi = new RosettaApi(
      configuration.baseUrl ?? "https://api.rosetta.careevolution.com",
      defaultHeaders,
    );
  }

  /**
   * Classifies a condition, problem, or diagnosis
   * @param request A FHIR Coding
   * @returns A set of key/value pairs representing different classification of the supplied coding
   */
  classifyCondition(request: ClassifyConditionRequest): Promise<ClassifyConditionResponse> {
    return this.rosettaApi.post("/terminology/v1/classify/condition", request);
  }

  /**
   * Classifies a medication
   * @param request A FHIR Coding
   * @returns A set of key/value pairs representing different classification of the supplied coding
   */
  classifyMedication(request: ClassifyMedicationRequest): Promise<ClassifyMedicationResponse> {
    return this.rosettaApi.post("/terminology/v1/classify/medication", request);
  }

  /**
   * Classifies an observation, including lab observations and panels, radiology or other reports
   * @param request A FHIR Coding
   * @returns A set of key/value pairs representing different classification of the supplied coding
   */
  classifyObservation(request: ClassifyObservationRequest): Promise<ClassifyObservationResponse> {
    return this.rosettaApi.post("/terminology/v1/classify/observation", request);
  }

  /**
   * Standardize a condition, problem, or diagnosis
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   */
  standardizeCondition(request: StandardizeRequest): Promise<StandardizeConditionResponse> {
    return this.rosettaApi.post("/terminology/v1/standardize/condition", request);
  }

  /**
   * Standardize a medication code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   */
  standardizeMedication(request: StandardizeRequest): Promise<StandardizeMedicationResponse> {
    return this.rosettaApi.post("/terminology/v1/standardize/medication", request);
  }

  /**
   * Standardize an observation code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   */
  standardizeObservation(request: StandardizeRequest): Promise<StandardizeObservationResponse> {
    return this.rosettaApi.post("/terminology/v1/standardize/observation", request);
  }

  /**
   * Standardize a procedure
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   */
  standardizeProcedure(request: StandardizeRequest): Promise<StandardizeObservationResponse> {
    return this.rosettaApi.post("/terminology/v1/standardize/procedure", request);
  }

  /**
   * Standardize a lab observation or report code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   */
  standardizeLab(request: StandardizeRequest): Promise<StandardizeLabResponse> {
    return this.rosettaApi.post("/terminology/v1/standardize/lab", request);
  }

  /**
   * Standardize a radiology or other report code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   */
  standardizeRadiology(request: StandardizeRequest): Promise<StandardizeRadiologyResponse> {
    return this.rosettaApi.post("/terminology/v1/standardize/radiology", request);
  }

  /**
   * Describes a code system
   * @param request A code system name
   * @returns A populated CodeSystem
   */
  getFhirR4CodeSystem(request: GetFhirR4CodeSystemRequest): Promise<GetFhirR4CodeSystemResponse> {
    const urlParameters = new URLSearchParams();
    if (request.pageNumber) {
      urlParameters.append("page.num", request.pageNumber.toString());
    }
    if (request.pageSize) {
      urlParameters.append("_count", request.pageSize.toString());
    }
    let route = `/terminology/v1/fhir/r4/codesystem/${request.codeSystem}`;
    const urlParametersString = urlParameters.toString();
    if (urlParametersString) {
      route += `?${urlParametersString}`;
    }
    return this.rosettaApi.get(route);
  }

  /**
   * Describes available code systems
   * @returns A bundle of known CodeSystems
   */
  summarizeFhirR4CodeSystems(): Promise<SummarizeFhirR4CodeSystemsResponse> {
    return this.rosettaApi.get("/terminology/v1/fhir/r4/codesystem?_summary=true");
  }

  /**
   * Describes available concept maps
   * @returns A bundle of known ConceptMaps
   */
  getFhirR4ConceptMaps(): Promise<GetFhirR4ConceptMapResponse> {
    return this.rosettaApi.get("/terminology/v1/fhir/r4/conceptmap");
  }

  /**
   * Standardizes source codings to a reference code
   * @param request The best source description of the concept
   * @returns A Parameters object with the `"result"` parameter of `"valueBoolean": true` indicating if the service was able to standardize the code
   */
  translateFhirR4ConceptMap(request: TranslateFhirR4ConceptMapRequest): Promise<TranslateFhirR4ConceptMapResponse> {
    let route = "/terminology/v1/fhir/r4/conceptmap/$translate";
    const urlParameters = new URLSearchParams({ code: request.code });
    if (request.domain) {
      urlParameters.append("domain", request.domain);
    }
    route += `?${urlParameters.toString()}`;
    return this.rosettaApi.get(route);
  }

  /**
   * Retrieves the set of ValueSets described in a scope
   * @param request A scope identifier
   * @returns A bundle of ValueSets within the requested scope
   */
  summarizeFhirR4ValueSetScope(request: SummarizeFhirR4ValueSetScopeRequest): Promise<SummarizeFhirR4ValueSetScopeResponse> {
    const params = new URLSearchParams({
      scope: request.scope,
      _summary: "true"
    });
    const route = `/terminology/v1/fhir/r4/valueset?${params.toString()}`;
    return this.rosettaApi.get(route);
  }

  /**
   * Summarizes the total number of codes in a ValueSet
   * @param request A ValueSet identifier
   * @returns
   */
  summarizeFhirR4ValueSet(request: SummarizeFhirR4ValueSetRequest): Promise<SummarizeFhirR4ValueSetResponse> {
    const parameters = new URLSearchParams({
      _summary: "true"
    });
    const route = `/terminology/v1/fhir/r4/valueset/${encodeURIComponent(request.id)}?${parameters.toString()}`;
    return this.rosettaApi.get(route);
  }

  /**
   * Retrieves a ValueSet by identifier
   * @param request A ValueSet identifier
   * @returns A ValueSet resource
   */
  getFhirR4ValueSet(request: GetFhirR4ValueSetRequest): Promise<GetFhirR4ValueSetResponse> {
    const route = `/terminology/v1/fhir/r4/valueset/${encodeURIComponent(request.id)}`;
    return this.rosettaApi.get(route);
  }

  /**
   * Retrieves a paginated list of ValueSets within a scope
   * @param request A paginated request for ValueSets within a scope
   * @returns A bundle of ValueSets within the requested scope
   */
  getFhirR4ValueSetScope(request: GetFhirR4ValueSetScopeRequest): Promise<GetFhirR4ValueSetScopeResponse> {
    const parameters = new URLSearchParams();
    if (request.pageNumber) {
      parameters.append("page.num", request.pageNumber.toString());
    }
    if (request.pageSize) {
      parameters.append("_count", request.pageSize.toString());
    }
    if (request.scope) {
      parameters.append("extension.scope", request.scope);
    }
    const route = `/terminology/v1/fhir/r4/valueset?${parameters.toString()}`;
    return this.rosettaApi.get(route);
  }

  /**
   * Requests the available ValueSet scopes
   * @returns A unique ValueSet that contains a list of all scopes available on the server
   */
  getFhirR4ValueSetScopes(): Promise<GetFhirR4ValueSetScopesResponse> {
    return this.rosettaApi.get("/terminology/v1/fhir/r4/valueset/Rosetta.ValueSetScopes");
  }

  /**
   * Determines which value sets contain the provided codes
   * @param request A Parameters resource containing codes to classify
   * @returns A Parameters resource containing the classification results
   */
  classifyFhirR4ValueSet(request: ClassifyFhirR4ValueSetMembershipRequest): Promise<ClassifyFhirR4ValueSetMembershipResponse> {
    const route = "/terminology/v1/fhir/r4/valueset/$classify";
    return this.rosettaApi.post(route, request);
  }

  /**
   * Computes an HCC Risk Adjustment Profile for the provided patient
   * @param request A FHIR R4 Bundle containing data for a single patient
   * @returns A new FHIR R4 Bundle containing measure and assessment resources
   */
  insightRiskProfile(request: InsightRiskProfileRequest): Promise<InsightRiskProfileResponse> {
    const parameters = new URLSearchParams();
    if (request.hccVersion) {
      parameters.append("hcc_version", request.hccVersion);
    }
    if (request.periodEndDate) {
      parameters.append("period_end_date", request.periodEndDate);
    }
    if (request.raSegment) {
      parameters.append("ra_segment", request.raSegment);
    }
    return this.rosettaApi.post(`/insight/v1/riskprofile?${parameters.toString()}`, request);
  }

  /**
   * Converts one or more HL7v2 messages into a FHIR R4 bundle
   * @param request A single or newline-delimited set of HL7v2.7 messages
   * @returns A FHIR R4 Bundle containing the clinical data parsed out of the HL7 messages
   */
  convertHl7ToFhirR4(request: ConvertHl7ToFhirR4Request): Promise<ConvertHl7ToFhirR4Response> {
    const headers = {
      "Content-Type": "text/plain",
    } as { [key: string]: string; };
    let route = "/convert/v1/hl7tofhirr4";
    if (request.patientID) {
      route += `/${encodeURIComponent(request.patientID)}`;
    }
    return this.rosettaApi.post(route, request.hl7Message, headers);
  }

  /**
   * Converts a CDA document into a FHIR R4 bundle
   * @param request A single CDA document
   * @returns A FHIR R4 Bundle containing the clinical data parsed out of the CDA
   */
  convertCdaToFhirR4(request: ConvertCdaToFhirR4Request): Promise<ConvertCdaToFhirR4Response> {
    const headers = {
      "Content-Type": "application/xml",
    } as { [key: string]: string; };
    let route = "/convert/v1/cdatofhirr4";
    if (request.patientID) {
      route += `/${encodeURIComponent(request.patientID)}`;
    }
    return this.rosettaApi.post(route, request.cda, headers);
  }

  /**
   * Converts a CDA document into a PDF document
   * @param request A single CDA document
   * @returns A formatted PDF document suitable for human review
   */
  convertCdaToPdf(request: ConvertCdaToPdfRequest): Promise<ConvertCdaToPdfResponse> {
    const headers = {
      "Content-Type": "application/xml",
      "Accept": "application/pdf",
    } as { [key: string]: string; };
    return this.rosettaApi.post("/convert/v1/cdatopdf", request.cda, headers);
  }

  /**
   * Converts a FHIR R4 bundle into an aggregated CDA document.
   * @param request A FHIR R4 bundle for a single patient
   * @returns An aggregated C-CDA R2.1 document in XML format
   */
  convertFhirR4ToCda(request: ConvertFhirR4ToCdaRequest): Promise<ConvertFhirR4ToCdaResponse> {
    const headers = {
      "Accept": "application/xml",
    } as { [key: string]: string; };
    return this.rosettaApi.post("/convert/v1/fhirr4tocda", request.fhirBundle, headers);
  }

  /**
   * Converts a FHIR R4 bundle into the OMOP Common Data Model v5.4 format.
   * @param request A FHIR R4 bundle for a single patient
   * @returns A ZIP archive containing multiple CSV files, one for each supported OMOP data table.
   */
  convertFhirR4ToOmop(request: ConvertFhirR4ToOmopRequest): Promise<ConvertFhirR4ToOmopResponse> {
    const headers = {
      "Accept": "application/zip",
    } as { [key: string]: string; };
    return this.rosettaApi.post("/convert/v1/fhirr4toomop", request.fhirBundle, headers);
  }

  /**
   * This operation aggregates information retrieved from prior Convert API requests into a single entry.
   * @param request A newline-delimited JSON list of FHIR R4 Bundles
   * @returns A single FHIR R4 Bundle containing the merged data from the input.
   */
  convertCombinedFhirR4Bundles(request: ConvertCombineFhirR4BundlesRequest): Promise<ConvertCombineFhirR4BundlesResponse> {
    const headers = {
      "Content-Type": "application/x-ndjson",
    } as { [key: string]: string; };
    let route = "/convert/v1/combinefhirbundles";
    if (request.personID) {
      route += `/${encodeURIComponent(request.personID)}`;
    }
    return this.rosettaApi.post(route, request.fhirBundles, headers);
  }

  /**
   * Summarizes a code system, typically used to determine number of codes
   * @param request A code system name
   * @returns An unpopulated CodeSystem
   */
  summarizeFhirR4CodeSystem(request: SummarizeFhirR4CodeSystemRequest): Promise<SummarizeFhirR4CodeSystemResponse> {
    const route = `/terminology/v1/fhir/r4/codesystem/${encodeURIComponent(request.codeSystem)}?_summary=true`;
    return this.rosettaApi.get(route);
  }
}

class RosettaApi {
  baseUrl: string;
  defaultHeaders: { [key: string]: string; };

  constructor(baseUrl: string, headers: { [key: string]: string; }) {
    this.baseUrl = baseUrl;
    this.defaultHeaders = headers;
  }

  private mergeHeaders(headers?: { [key: string]: string; }): { [key: string]: string; } {
    return {
      ...this.defaultHeaders,
      ...headers ?? {},
    };
  }

  async post(
    path: string,
    body: any, // eslint-disable-line @typescript-eslint/no-explicit-any
    headers?: { [key: string]: string; },
  ): Promise<any> { // eslint-disable-line @typescript-eslint/no-explicit-any
    const requestHeaders = this.mergeHeaders(headers);

    const preparedBody = requestHeaders["Content-Type"] === "application/json" ? JSON.stringify(body) : body;
    const url = this.baseUrl + path;

    const response = await fetch(url, {
      method: "POST",
      headers: requestHeaders,
      body: preparedBody,
    });
    if (!response.ok) {
      throw new Error(await response.text());
    }

    if (requestHeaders["Accept"] === "application/json") {
      return await response.json();
    }
    return await response.text();
  }

  async get(
    path: string,
    headers?: { [key: string]: string; },
  ): Promise<any> { // eslint-disable-line @typescript-eslint/no-explicit-any
    const requestHeaders = this.mergeHeaders(headers);

    const url = this.baseUrl + path;
    const response = await fetch(url, {
      method: "GET",
      headers: requestHeaders,
    });
    if (!response.ok) {
      console.log(response);
      throw new Error(await response.text());
    }

    return await response.json();
  }
}
