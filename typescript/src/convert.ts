import { Bundle } from "fhir/r4";

export type ConvertHl7ToFhirR4Request = {
  patientID?: string;
  hl7Message: string;
};

export type ConvertHl7ToFhirR4Response = Bundle;

export type ConvertCdaToFhirR4Request = {
  patientID?: string;
  cda: string;
};

export type ConvertCdaToFhirR4Response = Bundle;

export type ConvertCdaToFhirResponse = Bundle;

export type ConvertCdaToPdfRequest = {
  cda: string;
};

export type ConvertCdaToPdfResponse = string;

export type ConvertFhirR4ToCdaRequest = {
  fhirBundle: Bundle;
};

export type ConvertFhirR4ToCdaResponse = string;

export type ConvertFhirR4ToOmopRequest = {
  fhirBundle: Bundle;
};

export type ConvertFhirR4ToOmopResponse = string;

export type ConvertCombineFhirR4BundlesRequest = {
  personID?: string;
  fhirBundles: string;
};

export function generateConvertCombinedFhirBundlesRequestFromBundles(fhirBundles: Bundle[], personID?: string) {
  const bundles = fhirBundles.map((bundle) => JSON.stringify(bundle)).join("\n");
  return {
    personID: personID,
    fhirBundles: bundles,
  } as ConvertCombineFhirR4BundlesRequest;
}

export type ConvertCombineFhirR4BundlesResponse = Bundle;