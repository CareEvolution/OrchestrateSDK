import { Bundle } from "fhir/r4";
import { IHttpHandler } from "./httpHandler.js";

export type ConvertHl7ToFhirR4Request = {
  content: string;
  patientID?: string;
};

export type ConvertHl7ToFhirR4Response = Bundle;

export type ConvertCdaToFhirR4Request = {
  content: string;
  patientID?: string;
};

export type ConvertCdaToFhirR4Response = Bundle;

export type ConvertCdaToFhirResponse = Bundle;

export type ConvertCdaToPdfRequest = {
  content: string;
};

export type ConvertCdaToPdfResponse = Buffer;

export type ConvertFhirR4ToCdaRequest = {
  content: Bundle;
};

export type ConvertFhirR4ToCdaResponse = string;

export type ConvertFhirR4ToOmopRequest = {
  content: Bundle;
};

export type ConvertFhirR4ToOmopResponse = Buffer;

export type ConvertCombineFhirR4BundlesRequest = {
  content: string;
  patientID?: string;
};

export function generateConvertCombinedFhirBundlesRequestFromBundles(fhirBundles: Bundle[], personID?: string) {
  const bundles = fhirBundles.map((bundle) => JSON.stringify(bundle)).join("\n");
  return {
    patientID: personID,
    content: bundles,
  } as ConvertCombineFhirR4BundlesRequest;
}

export type ConvertCombineFhirR4BundlesResponse = Bundle;

export type ConvertX12ToFhirR4Request = {
  content: string;
  patientID?: string;
};

export type ConvertX12ToFhirR4Response = Bundle;


export class ConvertApi {
  private httpHandler: IHttpHandler;

  constructor(httpHandler: IHttpHandler) {
    this.httpHandler = httpHandler;
  }
  /**
   * Converts one or more HL7v2 messages into a FHIR R4 bundle
   * @param request A single or newline-delimited set of HL7v2.7 messages
   * @returns A FHIR R4 Bundle containing the clinical data parsed out of the HL7 messages
   * @link https://rosetta-api.docs.careevolution.com/convert/hl7_to_fhir.html
   */
  hl7ToFhirR4(request: ConvertHl7ToFhirR4Request): Promise<ConvertHl7ToFhirR4Response> {
    const headers = {
      "Content-Type": "text/plain",
    } as { [key: string]: string; };
    const parameters = new URLSearchParams();
    if (request.patientID) {
      parameters.append("patientId", request.patientID);
    }
    let route = "/convert/v1/hl7tofhirr4";
    if (parameters.size) {
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
  cdaToFhirR4(request: ConvertCdaToFhirR4Request): Promise<ConvertCdaToFhirR4Response> {
    const headers = {
      "Content-Type": "application/xml",
    } as { [key: string]: string; };
    const parameters = new URLSearchParams();
    if (request.patientID) {
      parameters.append("patientId", request.patientID);
    }
    let route = "/convert/v1/cdatofhirr4";
    if (parameters.size) {
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
  cdaToPdf(request: ConvertCdaToPdfRequest): Promise<ConvertCdaToPdfResponse> {
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
  fhirR4ToCda(request: ConvertFhirR4ToCdaRequest): Promise<ConvertFhirR4ToCdaResponse> {
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
  fhirR4ToOmop(request: ConvertFhirR4ToOmopRequest): Promise<ConvertFhirR4ToOmopResponse> {
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
  combineFhirR4Bundles(request: ConvertCombineFhirR4BundlesRequest): Promise<ConvertCombineFhirR4BundlesResponse> {
    const headers = {
      "Content-Type": "application/x-ndjson",
    } as { [key: string]: string; };
    const parameters = new URLSearchParams();
    if (request.patientID) {
      parameters.append("patientId", request.patientID);
    }
    let route = "/convert/v1/combinefhirr4bundles";
    if (parameters.size) {
      route += `?${parameters.toString()}`;
    }
    return this.httpHandler.post(route, request.content, headers);
  }

  /**
   * Converts an X12 document into a FHIR R4 bundle.
   * @param request A standard version 5010 X12 document
   * @returns A FHIR R4 Bundle containing the clinical data parsed out of the X12 messages
   */
  x12ToFhirR4(request: ConvertX12ToFhirR4Request): Promise<ConvertX12ToFhirR4Response> {
    const headers = {
      "Content-Type": "text/plain",
    } as { [key: string]: string; };
    const parameters = new URLSearchParams();
    if (request.patientID) {
      parameters.append("patientId", request.patientID);
    }
    let route = "/convert/v1/x12tofhirr4";
    if (parameters.size) {
      route += `?${parameters.toString()}`;
    }
    return this.httpHandler.post(route, request.content, headers);
  }
}