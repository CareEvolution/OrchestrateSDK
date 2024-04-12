import { Bundle, MeasureReport, Measure, Patient, RiskAssessment, OperationOutcome } from "fhir/r4.js";
import { IHttpHandler } from "./httpHandler.js";

const raSegments = [
  "community nondual aged",
  "community full benefit dual aged",
  "community full benefit dual disabled",
  "community nondual disabled",
  "long term institutional",
] as const;

const hccVersions = ["22", "23", "24"] as const;

export type InsightRiskProfileRequest = {
  content: Bundle;
  hccVersion?: (typeof hccVersions)[number];
  periodEndDate?: string;
  raSegment?: (typeof raSegments)[number];
};

export type InsightRiskProfileResource = Patient | MeasureReport | Measure | RiskAssessment | OperationOutcome;

export type InsightRiskProfileResponse = Bundle<InsightRiskProfileResource>;

export type InsightFhirR4ToManifestRequest = {
  content: Bundle;
};

export type InsightFhirR4ToManifestResponse = ArrayBuffer;

export class InsightApi {
  private httpHandler: IHttpHandler;

  constructor(httpHandler: IHttpHandler) {
    this.httpHandler = httpHandler;
  }
  /**
   * Computes an HCC Risk Adjustment Profile for the provided patient
   * @param request A FHIR R4 Bundle containing data for a single patient
   * @returns A new FHIR R4 Bundle containing measure and assessment resources
   * @link https://rosetta-api.docs.careevolution.com/insight/risk_profile.html
   */
  riskProfile(request: InsightRiskProfileRequest): Promise<InsightRiskProfileResponse> {
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
   * Generates a tabular report of clinical concepts from a FHIR R4 bundle. With this tabular data, you can easily scan results, run queries, and understand the value of your clinical data.
   * @param bundle A FHIR R4 Bundle
   * @returns A ZIP file containing a number of Comma-Separated Value (CSV) files corresponding to clinical concepts (conditions, encounters, etc.).
   * @link https://rosetta-api.docs.careevolution.com/insight/fhir_manifest.html
   */
  fhirR4ToManifest(request: InsightFhirR4ToManifestRequest): Promise<InsightFhirR4ToManifestResponse> {
    return this.httpHandler.post<Bundle, ArrayBuffer>(
      "/insight/v1/fhirr4tomanifest",
      request.content,
      { "Accept": "application/zip" }
    );
  }
}
