import type { Bundle } from "fhir/r4.js";
import { IHttpHandler } from "./httpHandler.js";

export type ConvertHl7ToFhirR4Request = {
  content: string;
  patientID?: string;
  tz?: string;
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

export type ConvertFhirDstu2ToFhirR4Request = {
  content: unknown;
};

export type ConvertFhirDstu2ToFhirR4Response = Bundle;

export type ConvertFhirStu3ToFhirR4Request = {
  content: unknown;
};

export type ConvertFhirStu3ToFhirR4Response = Bundle;

export type ConvertFhirR4ToHealthLakeRequest = {
  content: Bundle;
};

export type ConvertFhirR4ToHealthLakeResponse = Bundle;

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

export type ConvertCdaToHtmlRequest = {
  content: string;
};

export type ConvertCdaToHtmlResponse = string;

export type ConvertFhirR4ToNemsisV34Request = {
  content: Bundle;
};

export type ConvertFhirR4ToNemsisV34Response = string;

export type ConvertFhirR4ToNemsisV35Request = {
  content: Bundle;
};

export type ConvertFhirR4ToNemsisV35Response = string;

export class ConvertApi {
  private httpHandler: IHttpHandler;

  constructor(httpHandler: IHttpHandler) {
    this.httpHandler = httpHandler;
  }
  /**
   * Converts one or more HL7v2 messages into a FHIR R4 bundle
   * @param request A single or newline-delimited set of HL7v2.7 messages
   *  - `content` The HL7v2.7 messages to convert
   *  - `patientID` The patient ID to associate with the clinical data
   *  - `tz`: Default timezone for date-times in the HL7 when no timezone offset is present. Must be IANA or Windows timezone name. Defaults to UTC.
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
    if (request.tz) {
      parameters.append("tz", request.tz);
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
      Accept: "application/pdf",
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
      Accept: "application/xml",
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
      Accept: "application/zip",
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

  /**
   * Converts a FHIR DSTU2 bundle into a FHIR R4 bundle.
   * @param request The FHIR DSTU2 bundle to convert
   * @returns A FHIR R4 Bundle containing the clinical data parsed out of the FHIR DSTU2 bundle
   * @link https://orchestrate.docs.careevolution.com/convert/update_fhir_version.html
   */
  fhirDstu2ToFhirR4(request: ConvertFhirDstu2ToFhirR4Request): Promise<ConvertFhirDstu2ToFhirR4Response> {
    return this.httpHandler.post("/convert/v1/fhirdstu2tofhirr4", request.content);
  }

  /**
   * Converts a FHIR STU3 bundle into a FHIR R4 bundle.
   * @param request The FHIR STU3 bundle to convert
   * @returns A FHIR R4 Bundle containing the clinical data parsed out of the FHIR STU3 bundle
   * @link https://orchestrate.docs.careevolution.com/convert/update_fhir_version.html
   */
  fhirStu3ToFhirR4(request: ConvertFhirStu3ToFhirR4Request): Promise<ConvertFhirStu3ToFhirR4Response> {
    return this.httpHandler.post("/convert/v1/fhirstu3tofhirr4", request.content);
  }

  /**
   * This operation converts a FHIR R4 bundle from one of the other Orchestrate FHIR conversions (CDA-to-FHIR, HL7-to-FHIR, or Combine Bundles) into a form compatible with the Amazon HealthLake analysis platform.
   * @param request A FHIR R4 bundle for a single patient
   * @returns A FHIR R4 bundle of type collection, containing individual FHIR bundles compatible with the HealthLake API restrictions.
   * @link https://orchestrate.docs.careevolution.com/convert/fhir_to_health_lake.html
   */
  fhirR4ToHealthLake(request: ConvertFhirR4ToHealthLakeRequest): Promise<ConvertFhirR4ToHealthLakeResponse> {
    return this.httpHandler.post("/convert/v1/fhirr4tohealthlake", request.content);
  }

  /**
   * Converts a CDA document into human-readable HTML.
   * @param request A single CDA document
   * @returns A formatted HTML document suitable for human review
   * @link https://rosetta-api.docs.careevolution.com/convert/cda_to_html.html
   */
  cdaToHtml(request: ConvertCdaToHtmlRequest): Promise<ConvertCdaToHtmlResponse> {
    const headers = {
      "Content-Type": "application/xml",
      "Accept": "text/html",
    } as { [key: string]: string; };
    return this.httpHandler.post(
      "/convert/v1/cdatohtml",
      request.content,
      headers
    );
  }

  /**
   * Converts a FHIR R4 bundle (including one from CDA-to-FHIR, HL7-to-FHIR, or Combine Bundles) into the National Emergency Medical Services Information System (NEMSIS) XML format.
   * @param request A FHIR R4 bundle for a single patient. The bundle must contain at least one Encounter resource with a valid admission date.
   * @returns A NEMSIS v3.4 document in XML format.
   * @link https://orchestrate.docs.careevolution.com/convert/fhir_to_nemsis.html
   */
  fhirR4ToNemsisV34(request: ConvertFhirR4ToNemsisV34Request): Promise<ConvertFhirR4ToNemsisV34Response> {
    const headers = {
      "Accept": "application/xml",
    } as { [key: string]: string; };
    return this.httpHandler.post(
      "/convert/v1/fhirr4tonemsisv34",
      request.content,
      headers
    );
  }

  /**
   * Converts a FHIR R4 bundle (including one from CDA-to-FHIR, HL7-to-FHIR, or Combine Bundles) into the National Emergency Medical Services Information System (NEMSIS) XML format.
   * @param request A FHIR R4 bundle for a single patient. The bundle must contain at least one Encounter resource with a valid admission date.
   * @returns A NEMSIS v3.5 document in XML format.
   * @link https://orchestrate.docs.careevolution.com/convert/fhir_to_nemsis.html
   */
  fhirR4ToNemsisV35(request: ConvertFhirR4ToNemsisV35Request): Promise<ConvertFhirR4ToNemsisV35Response> {
    const headers = {
      "Accept": "application/xml",
    } as { [key: string]: string; };
    return this.httpHandler.post(
      "/convert/v1/fhirr4tonemsisv35",
      request.content,
      headers
    );
  }
}
