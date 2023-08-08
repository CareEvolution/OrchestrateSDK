import json
from orchestrate._internal.fhir import Bundle

ConvertHl7ToFhirR4Response = Bundle

ConvertCdaToFhirR4Response = Bundle

ConvertCdaToPdfResponse = bytes

ConvertFhirR4ToCdaResponse = str

ConvertFhirR4ToOmopResponse = bytes

ConvertX12ToFhirR4Response = Bundle


def generate_convert_combined_fhir_bundles_request_from_bundles(
    fhir_bundles: list[Bundle],
) -> str:
    """
    Converts a list of FHIR bundles into a request body for the combine FHIR bundles endpoint.

    ### Parameters

    - `fhir_bundles`: (list[Bundle]): A list of FHIR bundles.

    ### Returns

    The content of the request for the combined FHIR bundles endpoint.
    """
    return "\n".join([json.dumps(bundle) for bundle in fhir_bundles])
