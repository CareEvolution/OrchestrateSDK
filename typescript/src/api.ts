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
  ConvertX12ToFhirR4Request,
  ConvertX12ToFhirR4Response,
} from "./convert.js";
import { InsightRiskProfileRequest, InsightRiskProfileResponse } from "./insight.js";
import {
  ClassifyConditionRequest,
  ClassifyConditionResponse,
  ClassifyFhirR4ValueSetMembershipRequest as GetAllFhirR4ValueSetsForCodesRequest,
  ClassifyFhirR4ValueSetMembershipResponse as GetAllFhirR4ValueSetsForCodesResponse,
  ClassifyMedicationRequest,
  ClassifyMedicationResponse,
  ClassifyObservationRequest,
  ClassifyObservationResponse,
  GetFhirR4CodeSystemRequest,
  GetFhirR4CodeSystemResponse,
  GetFhirR4ConceptMapResponse,
  GetFhirR4ValueSetRequest,
  GetFhirR4ValueSetResponse,
  GetFhirR4ValueSetsByScopeRequest,
  GetFhirR4ValueSetsByScopeResponse,
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
} from "./terminology.js";

export interface Configuration {
  apiKey?: string;
  baseUrl?: string;
  additionalHeaders?: { [key: string]: string; };
}

type BatchResponse<T> = {
  items: T;
};

export class OrchestrateApi {
  httpHandler: HttpHandler;

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

    this.httpHandler = new HttpHandler(
      configuration.baseUrl ?? "https://api.careevolutionapi.com",
      defaultHeaders,
    );
  }

  async handleBatchOverload<TIn, TOut>(url: string, request: TIn): Promise<TOut> {
    if (Array.isArray(request)) {
      const batchResponse = await this.httpHandler.post(`${url}/batch`, { items: request });
      return (batchResponse as BatchResponse<TOut>).items;
    }
    return this.httpHandler.post(url, request);
  }

  /**
   * Classifies a condition, problem, or diagnosis. The input must be from one of the following code systems:
   *
   * - ICD-10-CM
   * - ICD-9-CM-Diagnosis
   * - SNOMED
   * @param request A FHIR Coding
   * @returns A set of key/value pairs representing different classification of the supplied coding
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/condition.html
  */
  classifyCondition(request: ClassifyConditionRequest): Promise<ClassifyConditionResponse>;
  /**
   * Classifies conditions, problems, or diagnoses. The input must be from one of the following code systems:
   * - ICD-10-CM
   * - ICD-9-CM-Diagnosis
   * - SNOMED
   * @param request An array of FHIR Codings
   * @returns An array of sets of key/value pairs representing different classification of the supplied coding in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/condition.html
   */
  classifyCondition(request: ClassifyConditionRequest[]): Promise<ClassifyConditionResponse[]>;
  classifyCondition(request: ClassifyConditionRequest | ClassifyConditionRequest[]): Promise<ClassifyConditionResponse | ClassifyConditionResponse[]> {
    return this.handleBatchOverload("/terminology/v1/classify/condition", request);
  }

  /**
   * Classifies a medication. The input must be from one of the following code systems:
   *
   * - RxNorm
   * - NDC
   * - CVX
   * - SNOMED
   * @param request A FHIR Coding
   * @returns A set of key/value pairs representing different classification of the supplied coding
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/medication.html
   */
  classifyMedication(request: ClassifyMedicationRequest): Promise<ClassifyMedicationResponse>;
  /**
   * Classifies medications. The input must be from one of the following code systems:
   *
   * - RxNorm
   * - NDC
   * - CVX
   * - SNOMED
   * @param request An array of FHIR Codings
   * @returns An array of sets of key/value pairs representing different classification of the supplied coding in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/medication.html
   */
  classifyMedication(request: ClassifyMedicationRequest[]): Promise<ClassifyMedicationResponse[]>;
  classifyMedication(request: ClassifyMedicationRequest | ClassifyMedicationRequest[]): Promise<ClassifyMedicationResponse | ClassifyMedicationResponse[]> {
    return this.handleBatchOverload("/terminology/v1/classify/medication", request);
  }

  /**
   * Classifies an observation, including lab observations and panels, radiology or other reports. The input must be from one of the following code systems:
   *
   * - LOINC
   * - SNOMED
   * @param request A FHIR Coding
   * @returns A set of key/value pairs representing different classification of the supplied coding
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/observation.html
   */
  classifyObservation(request: ClassifyObservationRequest): Promise<ClassifyObservationResponse>;
  /**
   * Classifies observations, including lab observations and panels, radiology or other reports. The input must be from one of the following code systems:
   *
   * - LOINC
   * - SNOMED
   * @param request An array of FHIR Codings
   * @returns An array of sets of key/value pairs representing different classification of the supplied coding in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/observation.html
   */
  classifyObservation(request: ClassifyObservationRequest[]): Promise<ClassifyObservationResponse[]>;
  classifyObservation(request: ClassifyObservationRequest | ClassifyObservationRequest[]): Promise<ClassifyObservationResponse | ClassifyObservationResponse[]> {
    return this.handleBatchOverload("/terminology/v1/classify/observation", request);
  }

  /**
   * Standardize a condition, problem, or diagnosis
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/condition.html
   */
  standardizeCondition(request: StandardizeRequest): Promise<StandardizeConditionResponse>;
  /**
   * Standardize conditions, problems, or diagnoses
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/condition.html
   */
  standardizeCondition(request: StandardizeRequest[]): Promise<StandardizeConditionResponse[]>;
  standardizeCondition(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeConditionResponse | StandardizeConditionResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/condition", request);
  }

  /**
   * Standardize a medication code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/medication.html
   */
  standardizeMedication(request: StandardizeRequest): Promise<StandardizeMedicationResponse>;
  /**
   * Standardize medication codes
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/medication.html
   */
  standardizeMedication(request: StandardizeRequest[]): Promise<StandardizeMedicationResponse[]>;
  standardizeMedication(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeMedicationResponse | StandardizeMedicationResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/medication", request);
  }

  /**
   * Standardize an observation code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/observation.html
   */
  standardizeObservation(request: StandardizeRequest): Promise<StandardizeObservationResponse>;
  /**
   * Standardize observation codes
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/observation.html
   */
  standardizeObservation(request: StandardizeRequest[]): Promise<StandardizeObservationResponse[]>;
  standardizeObservation(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeObservationResponse | StandardizeObservationResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/observation", request);
  }

  /**
   * Standardize a procedure
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/procedure.html
   */
  standardizeProcedure(request: StandardizeRequest): Promise<StandardizeObservationResponse>;
  /**
   * Standardize procedures
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/procedure.html
   */
  standardizeProcedure(request: StandardizeRequest[]): Promise<StandardizeObservationResponse[]>;
  standardizeProcedure(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeObservationResponse | StandardizeObservationResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/procedure", request);
  }

  /**
   * Standardize a lab observation or report code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/lab.html
   */
  standardizeLab(request: StandardizeRequest): Promise<StandardizeLabResponse>;
  /**
   * Standardize lab observations or report codes
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/lab.html
   */
  standardizeLab(request: StandardizeRequest[]): Promise<StandardizeLabResponse[]>;
  standardizeLab(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeLabResponse | StandardizeLabResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/lab", request);
  }

  /**
   * Standardize a radiology or other report code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/radiology.html
   */
  standardizeRadiology(request: StandardizeRequest): Promise<StandardizeRadiologyResponse>;
  /**
   * Standardize radiology or other report codes
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/radiology.html
   */
  standardizeRadiology(request: StandardizeRequest[]): Promise<StandardizeRadiologyResponse[]>;
  standardizeRadiology(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeRadiologyResponse | StandardizeRadiologyResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/radiology", request);
  }

  /**
   * Describes a code system
   * @param request A code system name
   * @returns A populated CodeSystem
   * @link https://rosetta-api.docs.careevolution.com/fhir/codesystem.html
   */
  getFhirR4CodeSystem(request: GetFhirR4CodeSystemRequest): Promise<GetFhirR4CodeSystemResponse> {
    const urlParameters = new URLSearchParams();
    if (request.pageNumber) {
      urlParameters.append("page.num", request.pageNumber.toString());
    }
    if (request.pageSize) {
      urlParameters.append("_count", request.pageSize.toString());
    }
    if (request.conceptContains) {
      urlParameters.append("concept:contains", request.conceptContains);
    }
    let route = `/terminology/v1/fhir/r4/codesystem/${request.codeSystem}`;
    const urlParametersString = urlParameters.toString();
    if (urlParametersString) {
      route += `?${urlParametersString}`;
    }
    return this.httpHandler.get(route);
  }

  /**
   * Describes available code systems
   * @returns A bundle of known CodeSystems
   * @link https://rosetta-api.docs.careevolution.com/fhir/codesystem.html
   */
  summarizeFhirR4CodeSystems(): Promise<SummarizeFhirR4CodeSystemsResponse> {
    return this.httpHandler.get("/terminology/v1/fhir/r4/codesystem?_summary=true");
  }

  /**
   * Describes available concept maps
   * @returns A bundle of known ConceptMaps
   * @link https://rosetta-api.docs.careevolution.com/fhir/conceptmap.html
   */
  getFhirR4ConceptMaps(): Promise<GetFhirR4ConceptMapResponse> {
    return this.httpHandler.get("/terminology/v1/fhir/r4/conceptmap");
  }

  /**
   * Standardizes source codings to a reference code
   * @param request The best source description of the concept
   * @returns A Parameters object with the `"result"` parameter of `"valueBoolean": true` indicating if the service was able to standardize the code
   * @link https://rosetta-api.docs.careevolution.com/fhir/conceptmap.html
   */
  translateFhirR4ConceptMap(request: TranslateFhirR4ConceptMapRequest): Promise<TranslateFhirR4ConceptMapResponse> {
    let route = "/terminology/v1/fhir/r4/conceptmap/$translate";
    const urlParameters = new URLSearchParams({ code: request.code });
    if (request.domain) {
      urlParameters.append("domain", request.domain);
    }
    route += `?${urlParameters.toString()}`;
    return this.httpHandler.get(route);
  }

  /**
   * Retrieves the set of ValueSets described in a scope
   * @param request A scope identifier
   * @returns A bundle of ValueSets within the requested scope
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  summarizeFhirR4ValueSetScope(request: SummarizeFhirR4ValueSetScopeRequest): Promise<SummarizeFhirR4ValueSetScopeResponse> {
    const params = new URLSearchParams({
      "extension.scope": request.scope,
      _summary: "true"
    });
    const route = `/terminology/v1/fhir/r4/valueset?${params.toString()}`;
    return this.httpHandler.get(route);
  }

  /**
   * Summarizes the total number of codes in a ValueSet
   * @param request A ValueSet identifier
   * @returns A ValueSet resource with only the count populated
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  summarizeFhirR4ValueSet(request: SummarizeFhirR4ValueSetRequest): Promise<SummarizeFhirR4ValueSetResponse> {
    const parameters = new URLSearchParams({
      _summary: "true"
    });
    const route = `/terminology/v1/fhir/r4/valueset/${encodeURIComponent(request.id)}?${parameters.toString()}`;
    return this.httpHandler.get(route);
  }

  /**
   * Retrieves a ValueSet by identifier
   * @param request A ValueSet identifier
   * @returns A ValueSet resource
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  getFhirR4ValueSet(request: GetFhirR4ValueSetRequest): Promise<GetFhirR4ValueSetResponse> {
    const route = `/terminology/v1/fhir/r4/valueset/${encodeURIComponent(request.id)}`;
    return this.httpHandler.get(route);
  }

  /**
   * Retrieves a paginated list of ValueSets filtered by name or scope
   * @param request A paginated request for ValueSets
   * @returns A bundle of ValueSets that match the search criteria
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  getFhirR4ValueSetsByScope(request: GetFhirR4ValueSetsByScopeRequest): Promise<GetFhirR4ValueSetsByScopeResponse> {
    const parameters = new URLSearchParams();
    if (request.name) {
      parameters.append("name", request.name);
    }
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
    return this.httpHandler.get(route);
  }

  /**
   * Requests the available ValueSet scopes
   * @returns A unique ValueSet that contains a list of all scopes available on the server
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  getFhirR4ValueSetScopes(): Promise<GetFhirR4ValueSetScopesResponse> {
    return this.httpHandler.get("/terminology/v1/fhir/r4/valueset/Rosetta.ValueSetScopes");
  }

  /**
   * In some situations it is useful to get the ValueSet(s) that a list of codes are members of. This can be used to categorize or group codes by ValueSet membership. For example, you may wish to:
   *
   *  - Categorize a collection of NDC drug codes by their active ingredient.
   *  - Categorize a collection of LOINC lab tests by the component they are measuring.
   *  - Categorize a collection of ICD-10-CM Diagnoses into a broad set of disease groupings.
   * @param request A Parameters resource containing codes to classify
   * @returns A Parameters resource containing the classification results
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  getAllFhirR4ValueSetsForCodes(request: GetAllFhirR4ValueSetsForCodesRequest): Promise<GetAllFhirR4ValueSetsForCodesResponse> {
    const route = "/terminology/v1/fhir/r4/valueset/$classify";
    return this.httpHandler.post(route, request);
  }

  /**
   * Computes an HCC Risk Adjustment Profile for the provided patient
   * @param request A FHIR R4 Bundle containing data for a single patient
   * @returns A new FHIR R4 Bundle containing measure and assessment resources
   * @link https://rosetta-api.docs.careevolution.com/insight/risk_profile.html
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
    let route = "/insight/v1/riskprofile";
    if (parameters.toString()) {
      route += `?${parameters.toString()}`;
    }
    return this.httpHandler.post(route, request.content);
  }

  /**
   * Converts one or more HL7v2 messages into a FHIR R4 bundle
   * @param request A single or newline-delimited set of HL7v2.7 messages
   * @returns A FHIR R4 Bundle containing the clinical data parsed out of the HL7 messages
   * @link https://rosetta-api.docs.careevolution.com/convert/hl7_to_fhir.html
   */
  convertHl7ToFhirR4(request: ConvertHl7ToFhirR4Request): Promise<ConvertHl7ToFhirR4Response> {
    const headers = {
      "Content-Type": "text/plain",
    } as { [key: string]: string; };
    const parameters = new URLSearchParams();
    if (request.patientID) {
      parameters.append("patientId", request.patientID);
    }
    let route = "/convert/v1/hl7tofhirr4";
    if (parameters.toString()) {
      route += `?${parameters.toString()}`;
    }
    return this.httpHandler.post(route, request.content, headers);
  }

  /**
   * Converts a CDA document into a FHIR R4 bundle
   * @param request A single CDA document
   * @returns A FHIR R4 Bundle containing the clinical data parsed out of the CDA
   * @link https://rosetta-api.docs.careevolution.com/convert/cda_to_fhir.html
   */
  convertCdaToFhirR4(request: ConvertCdaToFhirR4Request): Promise<ConvertCdaToFhirR4Response> {
    const headers = {
      "Content-Type": "application/xml",
    } as { [key: string]: string; };
    const parameters = new URLSearchParams();
    if (request.patientID) {
      parameters.append("patientId", request.patientID);
    }
    let route = "/convert/v1/cdatofhirr4";
    if (parameters.toString()) {
      route += `?${parameters.toString()}`;
    }
    return this.httpHandler.post(route, request.content, headers);
  }

  /**
   * Converts a CDA document into a PDF document
   * @param request A single CDA document
   * @returns A formatted PDF document suitable for human review
   * @link https://rosetta-api.docs.careevolution.com/convert/cda_to_pdf.html
   */
  convertCdaToPdf(request: ConvertCdaToPdfRequest): Promise<ConvertCdaToPdfResponse> {
    const headers = {
      "Content-Type": "application/xml",
      "Accept": "application/pdf",
    } as { [key: string]: string; };
    return this.httpHandler.post("/convert/v1/cdatopdf", request.content, headers);
  }

  /**
   * Converts a FHIR R4 bundle into an aggregated CDA document.
   * @param request A FHIR R4 bundle for a single patient
   * @returns An aggregated C-CDA R2.1 document in XML format
   * @link https://rosetta-api.docs.careevolution.com/convert/fhir_to_cda.html
   */
  convertFhirR4ToCda(request: ConvertFhirR4ToCdaRequest): Promise<ConvertFhirR4ToCdaResponse> {
    const headers = {
      "Accept": "application/xml",
    } as { [key: string]: string; };
    return this.httpHandler.post("/convert/v1/fhirr4tocda", request.content, headers);
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
    return this.httpHandler.post("/convert/v1/fhirr4toomop", request.content, headers);
  }

  /**
   * This operation aggregates information retrieved from prior Convert API requests into a single entry.
   * @param request A newline-delimited JSON list of FHIR R4 Bundles
   * @returns A single FHIR R4 Bundle containing the merged data from the input.
   * @link https://rosetta-api.docs.careevolution.com/convert/fhir_to_omop.html
   */
  convertCombinedFhirR4Bundles(request: ConvertCombineFhirR4BundlesRequest): Promise<ConvertCombineFhirR4BundlesResponse> {
    const headers = {
      "Content-Type": "application/x-ndjson",
    } as { [key: string]: string; };
    const parameters = new URLSearchParams();
    if (request.patientID) {
      parameters.append("patientId", request.patientID);
    }
    let route = "/convert/v1/combinefhirr4bundles";
    if (parameters.toString()) {
      route += `?${parameters.toString()}`;
    }
    return this.httpHandler.post(route, request.content, headers);
  }

  /**
   * Converts an X12 document into a FHIR R4 bundle.
   * @param request A standard version 5010 X12 document
   * @returns A FHIR R4 Bundle containing the clinical data parsed out of the X12 messages
   */
  convertX12ToFhirR4(request: ConvertX12ToFhirR4Request): Promise<ConvertX12ToFhirR4Response> {
    const headers = {
      "Content-Type": "text/plain",
    } as { [key: string]: string; };
    const parameters = new URLSearchParams();
    if (request.patientID) {
      parameters.append("patientId", request.patientID);
    }
    let route = "/convert/v1/x12tofhirr4";
    if (parameters.toString()) {
      route += `?${parameters.toString()}`;
    }
    return this.httpHandler.post(route, request.content, headers);
  }

  private getIDDependentRoute(route: string, id?: string): string {
    if (id) {
      return `${route}/${encodeURIComponent(id)}`;
    }
    return route;
  }

  /**
   * Summarizes a code system, typically used to determine number of codes
   * @param request A code system name
   * @returns An unpopulated CodeSystem
   * @link https://rosetta-api.docs.careevolution.com/fhir/codesystem.html
   */
  summarizeFhirR4CodeSystem(request: SummarizeFhirR4CodeSystemRequest): Promise<SummarizeFhirR4CodeSystemResponse> {
    const route = `/terminology/v1/fhir/r4/codesystem/${encodeURIComponent(request.codeSystem)}?_summary=true`;
    return this.httpHandler.get(route);
  }

}

class HttpHandler {
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

    if (requestHeaders["Accept"] === "application/zip" || requestHeaders["Accept"] === "application/pdf") {
      return await response.arrayBuffer();
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
      throw new Error(await response.text());
    }

    return await response.json();
  }
}
