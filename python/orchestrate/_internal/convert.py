from typing import Mapping, Optional
from urllib.parse import quote

from orchestrate._internal.fhir import Bundle
from orchestrate._internal.http_handler import HttpHandler

import json as _json
from orchestrate._internal.fhir import Bundle as Bundle

ConvertHl7ToFhirR4Response = Bundle

ConvertCdaToFhirR4Response = Bundle

ConvertCdaToPdfResponse = bytes

ConvertFhirR4ToCdaResponse = str

ConvertFhirR4ToOmopResponse = bytes

ConvertX12ToFhirR4Response = Bundle

ConvertCombinedFhirR4BundlesResponse = Bundle

ConvertFhirDstu2ToFhirR4Response = Bundle

ConvertFhirStu3ToFhirR4Response = Bundle

ConvertFhirR4ToHealthLakeResponse = Bundle

ConvertCdaToHtmlResponse = str

ConvertFhirR4ToNemsisV34Response = str

ConvertFhirR4ToNemsisV35Response = str

ConvertFhirR4ToManifestResponse = bytes


def generate_convert_combine_fhir_bundles_request_from_bundles(
    fhir_bundles: list[Bundle],
) -> str:
    """
    Converts a list of FHIR bundles into a request body for the combine FHIR bundles endpoint.

    ### Parameters

    - `fhir_bundles`: (list[Bundle]): A list of FHIR bundles.

    ### Returns

    The content of the request for the combined FHIR bundles endpoint.
    """
    return "\n".join([_json.dumps(bundle) for bundle in fhir_bundles])


def _get_id_dependent_parameters(
    id_name: str,
    id_: Optional[str] = None,
) -> dict[str, str]:
    if id_ is not None:
        return {id_name: id_}
    return {}


class ConvertApi:
    def __init__(self, http_handler: HttpHandler) -> None:
        self.__http_handler = http_handler

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(base_url={self.__http_handler.base_url!r})"

    def hl7_to_fhir_r4(
        self,
        content: str,
        patient_id: Optional[str] = None,
        patient_identifier: Optional[str] = None,
        patient_identifier_system: Optional[str] = None,
        tz: Optional[str] = None,
    ) -> ConvertHl7ToFhirR4Response:
        """
        Converts one or more HL7v2 messages into a FHIR R4 bundle

        ### Parameters

        - `hl7_message`: The HL7 message(s) to convert
        - `patient_id`: The patient ID to use for the FHIR bundle
        - `patient_identifier`: A patient identifier to add to identifier list of patient resource in the FHIR bundle. Must be specified along with patient_identifier_system
        - `patient_identifier_system`: The system providing the patient identifier. Must be specified along with patient_identifier
        - `tz`: Default timezone for date-times in the HL7 when no timezone offset is present. Must be IANA or Windows timezone name. Defaults to UTC.

        ### Returns

        A FHIR R4 Bundle containing the clinical data parsed out of the HL7 messages

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/hl7_to_fhir.html>
        """
        headers = {"Content-Type": "text/plain"}
        parameters = _get_id_dependent_parameters("patientId", patient_id)
        parameters = {
            **parameters,
            **_get_id_dependent_parameters("patientIdentifier", patient_identifier),
        }
        parameters = {
            **parameters,
            **_get_id_dependent_parameters(
                "patientIdentifierSystem", patient_identifier_system
            ),
        }
        parameters = {**parameters, **_get_id_dependent_parameters("tz", tz)}
        return self.__http_handler.post(
            path="/convert/v1/hl7tofhirr4",
            body=content,
            headers=headers,
            parameters=parameters,
        )

    def cda_to_fhir_r4(
        self,
        content: str,
        patient_id: Optional[str] = None,
        patient_identifier: Optional[str] = None,
        patient_identifier_system: Optional[str] = None,
    ) -> ConvertCdaToFhirR4Response:
        """
        Converts a CDA document into a FHIR R4 bundle

        ### Parameters

        - `cda`: The CDA document to convert
        - `patient_id`: The patient ID to use for the FHIR bundle
        - `patient_identifier`: A patient identifier to add to identifier list of patient resource in the FHIR bundle. Must be specified along with patient_identifier_system
        - `patient_identifier_system`: The system providing the patient identifier. Must be specified along with patient_identifier

        ### Returns

        A FHIR R4 Bundle containing the clinical data parsed out of the CDA

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/cda_to_fhir.html>
        """
        headers = {"Content-Type": "application/xml"}
        parameters = _get_id_dependent_parameters("patientId", patient_id)
        parameters = {
            **parameters,
            **_get_id_dependent_parameters("patientIdentifier", patient_identifier),
        }
        parameters = {
            **parameters,
            **_get_id_dependent_parameters(
                "patientIdentifierSystem", patient_identifier_system
            ),
        }
        return self.__http_handler.post(
            path="/convert/v1/cdatofhirr4",
            body=content,
            headers=headers,
            parameters=parameters,
        )

    def cda_to_pdf(self, content: str) -> ConvertCdaToPdfResponse:
        """
        Converts a CDA document into a PDF document

        ### Parameters

        - `cda`: The CDA document to convert

        ### Returns

        A formatted PDF document suitable for human review

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/cda_to_pdf.html>
        """
        headers = {"Content-Type": "application/xml", "Accept": "application/pdf"}
        response = self.__http_handler.post(
            path="/convert/v1/cdatopdf",
            body=content,
            headers=headers,
        )
        return response

    def fhir_r4_to_cda(self, content: Bundle) -> ConvertFhirR4ToCdaResponse:
        """
        Converts a FHIR R4 bundle into an aggregated CDA document.

        ### Parameters

        - `fhir_bundle`: A FHIR R4 bundle for a single patient

        ### Returns

        An aggregated C-CDA R2.1 document in XML format

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/fhir_to_cda.html>
        """
        headers = {"Accept": "application/xml"}
        return self.__http_handler.post(
            path="/convert/v1/fhirr4tocda",
            body=content,
            headers=headers,
        )

    def fhir_r4_to_omop(self, content: Bundle) -> ConvertFhirR4ToOmopResponse:
        """
        Converts a FHIR R4 bundle into the OMOP Common Data Model v5.4 format.

        ### Parameters

        - `fhir_bundle`: A FHIR R4 bundle for a single patient

        ### Returns

        A ZIP archive containing multiple CSV files, one for each supported OMOP data table.

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/fhir_to_omop.html>
        """
        headers = {
            "Accept": "application/zip",
        }
        response = self.__http_handler.post(
            path="/convert/v1/fhirr4toomop",
            body=content,
            headers=headers,
        )
        return response

    def x12_to_fhir_r4(
        self,
        content: str,
        patient_id: Optional[str] = None,
        patient_identifier: Optional[str] = None,
        patient_identifier_system: Optional[str] = None,
    ) -> ConvertX12ToFhirR4Response:
        """
        Converts an X12 document into a FHIR R4 bundle

        ### Parameters

        - `x12_document`: The X12 document to convert
        - `patient_id`: The patient ID to use for the FHIR bundle
        - `patient_identifier`: A patient identifier to add to identifier list of patient resource in the FHIR bundle. Must be specified along with patient_identifier_system
        - `patient_identifier_system`: The system providing the patient identifier. Must be specified along with patient_identifier

        ### Returns

        A FHIR R4 Bundle containing the clinical data parsed out of the X12
        """
        headers = {"Content-Type": "text/plain"}
        parameters = _get_id_dependent_parameters("patientId", patient_id)
        parameters = {
            **parameters,
            **_get_id_dependent_parameters("patientIdentifier", patient_identifier),
        }
        parameters = {
            **parameters,
            **_get_id_dependent_parameters(
                "patientIdentifierSystem", patient_identifier_system
            ),
        }
        return self.__http_handler.post(
            path="/convert/v1/x12tofhirr4",
            body=content,
            headers=headers,
            parameters=parameters,
        )

    def combine_fhir_r4_bundles(
        self,
        content: str,
        patient_id: Optional[str] = None,
        patient_identifier: Optional[str] = None,
        patient_identifier_system: Optional[str] = None,
    ) -> ConvertCombinedFhirR4BundlesResponse:
        """
        This operation aggregates information retrieved from prior Convert API requests into a single entry.

        ### Parameters

        - `fhir_bundles`: A newline-delimited JSON list of FHIR R4 Bundles
        - `patient_id`: The patient ID to use for the FHIR bundle
        - `patient_identifier`: A patient identifier to add to identifier list of patient resource in the FHIR bundle. Must be specified along with patient_identifier_system
        - `patient_identifier_system`: The system providing the patient identifier. Must be specified along with patient_identifier

        ### Returns

        A single FHIR R4 Bundle containing the merged data from the input.

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/combine_bundles.html>
        """
        headers = {"Content-Type": "application/x-ndjson"}
        parameters = _get_id_dependent_parameters("patientId", patient_id)
        parameters = {
            **parameters,
            **_get_id_dependent_parameters("patientIdentifier", patient_identifier),
        }
        parameters = {
            **parameters,
            **_get_id_dependent_parameters(
                "patientIdentifierSystem", patient_identifier_system
            ),
        }
        return self.__http_handler.post(
            path="/convert/v1/combinefhirr4bundles",
            body=content,
            headers=headers,
            parameters=parameters,
        )

    def fhir_dstu2_to_fhir_r4(
        self,
        content: Bundle,
    ) -> ConvertFhirDstu2ToFhirR4Response:
        """
        Converts a FHIR DSTU2 bundle into a FHIR R4 bundle

        ### Parameters

        - `fhir_dstu2_bundle`: The FHIR DSTU2 bundle to convert

        ### Returns

        A FHIR R4 Bundle containing the clinical data parsed out of the FHIR DSTU2 bundle

        ### Documentation

        <https://orchestrate.docs.careevolution.com/convert/update_fhir_version.html>
        """
        return self.__http_handler.post(
            path="/convert/v1/fhirdstu2tofhirr4",
            body=content,
        )

    def fhir_stu3_to_fhir_r4(
        self,
        content: Bundle,
    ) -> ConvertFhirStu3ToFhirR4Response:
        """
        Converts a FHIR STU3 bundle into a FHIR R4 bundle

        ### Parameters

        - `fhir_stu3_bundle`: The FHIR STU3 bundle to convert

        ### Returns

        A FHIR R4 Bundle containing the clinical data parsed out of the FHIR STU3 bundle

        ### Documentation

        <https://orchestrate.docs.careevolution.com/convert/update_fhir_version.html>
        """
        return self.__http_handler.post(
            path="/convert/v1/fhirstu3tofhirr4",
            body=content,
        )

    def fhir_r4_to_health_lake(
        self,
        content: Bundle,
    ) -> ConvertFhirR4ToHealthLakeResponse:
        """
        This operation converts a FHIR R4 bundle from one of the other Orchestrate FHIR conversions (CDA-to-FHIR, HL7-to-FHIR, or Combine Bundles) into a form compatible with the Amazon HealthLake analysis platform.

        ### Parameters

        - `content`: A FHIR R4 bundle for a single patient

        ### Returns

        A FHIR R4 bundle of type collection, containing individual FHIR bundles compatible with the HealthLake API restrictions.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/convert/fhir_to_health_lake.html>
        """
        return self.__http_handler.post(
            path="/convert/v1/fhirr4tohealthlake",
            body=content,
        )

    def cda_to_html(self, content: str) -> ConvertCdaToHtmlResponse:
        """
        Converts a CDA document into human-readable HTML.

        ### Parameters

        - `content`: A single CDA document

        ### Returns

        A formatted HTML document suitable for human review

        ### Documentation

        <https://orchestrate.docs.careevolution.com/convert/cda_to_html.html>
        """
        headers = {"Content-Type": "application/xml", "Accept": "text/html"}
        return self.__http_handler.post(
            path="/convert/v1/cdatohtml",
            body=content,
            headers=headers,
        )

    def fhir_r4_to_nemsis_v34(
        self, content: Bundle
    ) -> ConvertFhirR4ToNemsisV34Response:
        """
        Converts a FHIR R4 bundle (including one from CDA-to-FHIR, HL7-to-FHIR, or Combine Bundles) into the National Emergency Medical Services Information System (NEMSIS) XML format.

        ### Parameters

        - `fhir_bundle`: A FHIR R4 bundle for a single patient. The bundle must contain at least one Encounter resource with a valid admission date.

        ### Returns

        A NEMSIS v3.4 document in XML format.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/convert/fhir_to_nemsis.html>
        """
        headers = {"Accept": "application/xml"}
        return self.__http_handler.post(
            path="/convert/v1/fhirr4tonemsisv34",
            body=content,
            headers=headers,
        )

    def fhir_r4_to_nemsis_v35(
        self, content: Bundle
    ) -> ConvertFhirR4ToNemsisV35Response:
        """
        Converts a FHIR R4 bundle (including one from CDA-to-FHIR, HL7-to-FHIR, or Combine Bundles) into the National Emergency Medical Services Information System (NEMSIS) XML format.

        ### Parameters

        - `fhir_bundle`: A FHIR R4 bundle for a single patient. The bundle must contain at least one Encounter resource with a valid admission date.

        ### Returns

        A NEMSIS v3.5 document in XML format.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/convert/fhir_to_nemsis.html>
        """
        headers = {"Accept": "application/xml"}
        return self.__http_handler.post(
            path="/convert/v1/fhirr4tonemsisv35",
            body=content,
            headers=headers,
        )

    def fhir_r4_to_manifest(
        self, content: Bundle, delimiter: Optional[str] = None
    ) -> ConvertFhirR4ToManifestResponse:
        """
        Generates a tabular report of clinical concepts from a FHIR R4
        bundle. With this tabular data, you can easily scan results, run
        queries, and understand the value of your clinical data.

        ### Parameters

        - `content`: A FHIR R4 bundle
        - `delimiter`: The delimiter to use in the CSV files. Allowed delimiters are | or ~ or ^ or ; Default delimiter is ,

        ### Returns

        A ZIP file containing a number of Comma-Separated Value (CSV)
        files corresponding to clinical concepts (conditions,
        encounters, etc.).

        ### Documentation

        <https://orchestrate.docs.careevolution.com/convert/fhir_manifest.html>
        """
        headers = {
            "Accept": "application/zip",
        }
        parameters = _get_id_dependent_parameters("delimiter", delimiter)
        return self.__http_handler.post(
            path="/convert/v1/fhirr4tomanifest",
            body=content,
            headers=headers,
            parameters=parameters,
        )
