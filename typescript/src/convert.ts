import { Bundle } from "fhir/r4";

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
  personID?: string;
};

export function generateConvertCombinedFhirBundlesRequestFromBundles(fhirBundles: Bundle[], personID?: string) {
  const bundles = fhirBundles.map((bundle) => JSON.stringify(bundle)).join("\n");
  return {
    personID: personID,
    content: bundles,
  } as ConvertCombineFhirR4BundlesRequest;
}

export type ConvertCombineFhirR4BundlesResponse = Bundle;

export type ConvertX12ToFhirR4Request = {
  content: string;
  patientID?: string;
};

export type ConvertX12ToFhirR4Response = Bundle;