import json
from typing import Any, Literal, Mapping, Optional
from urllib.parse import quote

import requests
from orchestrate.convert import (
    ConvertCdaToFhirR4Response,
    ConvertCdaToPdfResponse,
    ConvertFhirR4ToCdaResponse,
    ConvertFhirR4ToOmopResponse,
    ConvertHl7ToFhirR4Response,
    ConvertX12ToFhirR4Response,
)
from orchestrate._internal.fhir import Bundle, Parameters
from orchestrate.insight import InsightRiskProfileResponse
from orchestrate.terminology import (
    ClassifyConditionResponse,
    ClassifyConditionSystems,
    ClassifyMedicationResponse,
    ClassifyMedicationSystems,
    ClassifyObservationResponse,
    ClassifyObservationSystems,
    CodeSystems,
    ConvertCombinedFhirR4BundlesResponse,
    GetAllFhirR4ValueSetsForCodesResponse,
    GetFhirR4CodeSystemResponse,
    GetFhirR4ValueSetResponse,
    GetFhirR4ValueSetScopesResponse,
    GetFhirR4ValueSetsByScopeResponse,
    StandardizeConditionResponse,
    StandardizeMedicationResponse,
    StandardizeTargetSystems,
    SummarizeFhirR4CodeSystemResponse,
    SummarizeFhirR4CodeSystemsResponse,
    SummarizeFhirR4ValueSetResponse,
    SummarizeFhirR4ValueSetScopeResponse,
    TranslateDomains,
    TranslateFhirR4ConceptMapResponse,
)


class _RosettaApi:
    def __init__(
        self,
        base_url: str,
        default_headers: dict,
    ) -> None:
        self._base_url = base_url
        self.__default_headers = default_headers

    def __merge_headers(self, headers: Optional[dict]) -> dict:
        if headers is None:
            return self.__default_headers
        return {**self.__default_headers, **headers}

    def _post(
        self,
        path: str,
        body: Any,
        headers: Optional[dict[str, str]] = None,
        parameters: Optional[dict[str, Optional[str]]] = None,
    ) -> Any:
        request_headers = self.__merge_headers(headers)

        prepared_body = (
            json.dumps(body)
            if request_headers["Content-Type"] == "application/json"
            else body
        )
        url = f"{self._base_url}{path}"

        response = requests.post(
            url,
            data=prepared_body,
            headers=request_headers,
            params=parameters,
        )
        response.raise_for_status()

        if (
            request_headers["Accept"] in ["application/zip", "application/pdf"]
        ) and response.content:
            return response.content

        if (request_headers["Accept"] == "application/json") and response.text:
            return response.json()

        return response.text

    def _get(
        self,
        path: str,
        headers: Optional[dict] = None,
        parameters: Optional[Mapping[str, Optional[str]]] = None,
    ) -> Any:
        request_headers = self.__merge_headers(headers)

        url = f"{self._base_url}{path}"
        response = requests.get(
            url,
            headers=request_headers,
            params=parameters,
        )
        response.raise_for_status()

        if (request_headers["Accept"] == "application/json") and response.text:
            return response.json()

        return response.text


def _get_coding_body(
    code: Optional[str] = None,
    system: Optional[str] = None,
    display: Optional[str] = None,
) -> dict[str, str]:
    body = {}
    if code is not None:
        body["code"] = code
    if system is not None:
        body["system"] = system
    if display is not None:
        body["display"] = display

    return body


def _get_pagination_parameters(
    page_number: Optional[int] = None,
    page_size: Optional[int] = None,
) -> dict[str, Optional[str]]:
    parameters = {
        "page.num": str(page_number) if page_number is not None else None,
        "_count": str(page_size) if page_size is not None else None,
    }
    return parameters


def _get_id_dependent_route(
    route: str,
    id_: Optional[str] = None,
) -> str:
    if id_ is not None:
        route += f"/{quote(id_)}"
    return route


class OrchestrateApi(_RosettaApi):
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        additional_headers: Optional[dict] = None,
    ) -> None:
        default_headers = {
            **(additional_headers or {}),
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if api_key is not None:
            default_headers["x-api-key"] = api_key

        super().__init__(
            base_url=base_url or "https://api.rosetta.careevolution.com",
            default_headers=default_headers,
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(base_url={self._base_url!r})"

    def classify_condition(
        self,
        code: str,
        system: ClassifyConditionSystems,
        display: Optional[str] = None,
    ) -> ClassifyConditionResponse:
        """
        Classifies a condition, problem, or diagnosis. The input must be from
        one of the following code systems:

        - ICD-10-CM
        - ICD-9-CM-Diagnosis
        - SNOMED

        ### Parameters

        - `code`: The code of the condition, problem, or diagnosis
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding's code

        ### Returns

        A set of key/value pairs representing different classification of the supplied coding

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/condition.html>
        """
        body = _get_coding_body(code, system, display)
        return self._post("/terminology/v1/classify/condition", body)

    def classify_medication(
        self,
        code: str,
        system: ClassifyMedicationSystems,
        display: Optional[str] = None,
    ) -> ClassifyMedicationResponse:
        """
        Classifies a medication. The input must be from one of the following code systems:

        - RxNorm
        - NDC
        - CVX
        - SNOMED

        ### Parameters

        - `code`: The code of the medication
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A set of key/value pairs representing different classification of the supplied coding

        ### Documenation

        <
        """
        body = _get_coding_body(code, system, display)
        return self._post("/terminology/v1/classify/medication", body)

    def classify_observation(
        self,
        code: str,
        system: ClassifyObservationSystems,
        display: Optional[str] = None,
    ) -> ClassifyObservationResponse:
        """
        Classifies an observation, including lab observations and panels,
        radiology or other reports. The input must be from one of the following
        code systems:

        - LOINC
        - SNOMED

        ### Parameters

        - `code`: The code of the observation
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A set of key/value pairs representing different classification of the supplied coding

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/observation.html>
        """
        body = _get_coding_body(code, system, display)
        return self._post("/terminology/v1/classify/observation", body)

    def standardize_condition(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeConditionResponse:
        """
        Standardize a condition, problem, or diagnosis

        ### Parameters

        - `code`: The code of the condition, problem, or diagnosis
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding's code

        ### Returns

        A collection of standardized codes

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/condition.html>
        """
        body = _get_coding_body(code, system, display)
        return self._post("/terminology/v1/standardize/condition", body)

    def standardize_medication(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeMedicationResponse:
        """
        Standardize a medication code

        ### Parameters

        - `code`: The code of the medication
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A collection of standardized codes

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/medication.html>
        """
        body = _get_coding_body(code, system, display)
        return self._post("/terminology/v1/standardize/medication", body)

    def standardize_observation(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeMedicationResponse:
        """
        Standardize an observation code

        ### Parameters

        - `code`: The code of the observation
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A collection of standardized codes

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/observation.html>
        """
        body = _get_coding_body(code, system, display)
        return self._post("/terminology/v1/standardize/observation", body)

    def standardize_procedure(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeMedicationResponse:
        """
        Standardize a procedure code

        ### Parameters

        - `code`: The code of the procedure
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A collection of standardized codes

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/procedure.html>
        """
        body = _get_coding_body(code, system, display)
        return self._post("/terminology/v1/standardize/procedure", body)

    def standardize_lab(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeMedicationResponse:
        """
        Standardize a lab code

        ### Parameters

        - `code`: The code of the lab
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A collection of standardized codes

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/lab.html>
        """
        body = _get_coding_body(code, system, display)
        return self._post("/terminology/v1/standardize/lab", body)

    def standardize_radiology(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeMedicationResponse:
        """
        Standardize a radiology code

        ### Parameters

        - `code`: The code of the radiology
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A collection of standardized codes

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/radiology.html>
        """
        body = _get_coding_body(code, system, display)
        return self._post("/terminology/v1/standardize/radiology", body)

    def convert_hl7_to_fhir_r4(
        self,
        hl7_message: str,
        patient_id: Optional[str] = None,
    ) -> ConvertHl7ToFhirR4Response:
        """
        Converts one or more HL7v2 messages into a FHIR R4 bundle

        ### Parameters

        - `hl7_message`: The HL7 message(s) to convert
        - `patient_id`: The patient ID to use for the FHIR bundle

        ### Returns

        A FHIR R4 Bundle containing the clinical data parsed out of the HL7 messages

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/convert/hl7_to_fhir.html>
        """
        headers = {"Content-Type": "text/plain"}
        route = _get_id_dependent_route("/convert/v1/hl7tofhirr4", patient_id)
        return self._post(
            path=route,
            body=hl7_message,
            headers=headers,
        )

    def convert_cda_to_fhir_r4(
        self,
        cda: str,
        patient_id: Optional[str] = None,
    ) -> ConvertCdaToFhirR4Response:
        """
        Converts a CDA document into a FHIR R4 bundle

        ### Parameters

        - `cda`: The CDA document to convert
        - `patient_id`: The patient ID to use for the FHIR bundle

        ### Returns

        A FHIR R4 Bundle containing the clinical data parsed out of the CDA

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/convert/cda_to_fhir.html>
        """
        headers = {"Content-Type": "application/xml"}
        route = _get_id_dependent_route("/convert/v1/cdatofhirr4", patient_id)
        return self._post(
            path=route,
            body=cda,
            headers=headers,
        )

    def convert_cda_to_pdf(self, cda: str) -> ConvertCdaToPdfResponse:
        """
        Converts a CDA document into a PDF document

        ### Parameters

        - `cda`: The CDA document to convert

        ### Returns

        A formatted PDF document suitable for human review

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/convert/cda_to_pdf.html>
        """
        headers = {"Content-Type": "application/xml", "Accept": "application/pdf"}
        response = self._post(
            path="/convert/v1/cdatopdf",
            body=cda,
            headers=headers,
        )
        return response

    def convert_fhir_r4_to_cda(self, fhir_bundle: Bundle) -> ConvertFhirR4ToCdaResponse:
        """
        Converts a FHIR R4 bundle into an aggregated CDA document.

        ### Parameters

        - `fhir_bundle`: A FHIR R4 bundle for a single patient

        ### Returns

        An aggregated C-CDA R2.1 document in XML format

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/convert/fhir_to_cda.html>
        """
        headers = {"Accept": "application/xml"}
        return self._post(
            path="/convert/v1/fhirr4tocda",
            body=fhir_bundle,
            headers=headers,
        )

    def convert_fhir_r4_to_omop(
        self, fhir_bundle: Bundle
    ) -> ConvertFhirR4ToOmopResponse:
        """
        Converts a FHIR R4 bundle into the OMOP Common Data Model v5.4 format.

        ### Parameters

        - `fhir_bundle`: A FHIR R4 bundle for a single patient

        ### Returns

        A ZIP archive containing multiple CSV files, one for each supported OMOP data table.

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/convert/fhir_to_omop.html>
        """
        headers = {
            "Accept": "application/zip",
        }
        response = self._post(
            path="/convert/v1/fhirr4toomop",
            body=fhir_bundle,
            headers=headers,
        )
        return response

    def convert_x12_to_fhir_r4(
        self,
        x12_document: str,
        patient_id: Optional[str] = None,
    ) -> ConvertX12ToFhirR4Response:
        """
        Converts an X12 document into a FHIR R4 bundle

        ### Parameters

        - `x12_document`: The X12 document to convert
        - `patient_id`: The patient ID to use for the FHIR bundle

        ### Returns

        A FHIR R4 Bundle containing the clinical data parsed out of the X12
        """
        headers = {"Content-Type": "text/plain"}
        route = _get_id_dependent_route("/convert/v1/x12tofhirr4", patient_id)
        return self._post(
            path=route,
            body=x12_document,
            headers=headers,
        )

    def insight_risk_profile(
        self,
        fhir_bundle: Bundle,
        hcc_version: Optional[Literal["22", "23", "24"]] = None,
        period_end_date: Optional[str] = None,
        ra_segment: Optional[
            Literal[
                "community nondual aged",
                "community full benefit dual aged",
                "community full benefit dual disabled",
                "community nondual disabled",
                "long term institutional",
            ]
        ] = None,
    ) -> InsightRiskProfileResponse:
        """
        Computes an HCC Risk Adjustment Profile for the provided patient

        ### Parameters

        - `fhir_bundle`: A FHIR R4 bundle for a single patient
        - `hcc_version`: The HCC version to use
        - `period_end_date`: The period end date to use
        - `ra_segment`: The risk adjustment segment to use

        ### Returns

        A new FHIR R4 Bundle containing measure and assessment resources

        ### Documenation

        <
        """
        parameters = {
            "hccVersion": hcc_version,
            "periodEndDate": period_end_date,
            "raSegment": ra_segment,
        }
        return self._post(
            path="/insight/v1/riskprofile",
            body=fhir_bundle,
            parameters=parameters,
        )

    def get_fhir_r4_code_system(
        self,
        code_system: CodeSystems,
        concept_contains: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> GetFhirR4CodeSystemResponse:
        """
        Describes a code system

        ### Parameters

        - `code_system`: The CodeSystem to retrieve
        - `page_number`: When paginating, the page number to retrieve
        - `page_size`: When paginating, The page size to retrieve

        ### Returns

        A FHIR R4 CodeSystem resource

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/fhir/codesystem.html>
        """
        parameters = _get_pagination_parameters(page_number, page_size)
        if concept_contains is not None:
            parameters["concept:contains"] = concept_contains

        return self._get(
            path=f"/terminology/v1/fhir/r4/codesystem/{code_system}",
            parameters=parameters,
        )

    def summarize_fhir_r4_code_systems(self) -> SummarizeFhirR4CodeSystemsResponse:
        """
        Describes available code systems

        ### Returns

        A bundle of known CodeSystems

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/fhir/codesystem.html>
        """
        return self._get(
            path="/terminology/v1/fhir/r4/codesystem", parameters={"_summary": "true"}
        )

    def get_fhir_r4_concept_maps(
        self,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> GetFhirR4CodeSystemResponse:
        """
        Describes available concept maps

        ### Returns

        A bundle of known ConceptMaps

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/fhir/conceptmap.html>
        """
        return self._get(path=f"/terminology/v1/fhir/r4/conceptmap")

    def translate_fhir_r4_concept_map(
        self,
        code: str,
        domain: Optional[TranslateDomains] = None,
    ) -> TranslateFhirR4ConceptMapResponse:
        """
        Standardizes source codings to a reference code

        ### Parameters

        - `code`: The code of the condition, problem, or diagnosis
        - `domain`: The source domain of the code

        ### Returns

        A Parameters object with the `"result"` parameter of `"valueBoolean": true` indicating if the service was able to standardize the code

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/fhir/conceptmap.html>
        """
        parameters = {
            "code": code,
            "domain": domain,
        }
        return self._get(
            path="/terminology/v1/fhir/r4/conceptmap/$translate",
            parameters=parameters,
        )

    def summarize_fhir_r4_value_set_scope(
        self, scope: str
    ) -> SummarizeFhirR4ValueSetScopeResponse:
        """
        Retrieves the set of ValueSets described in a scope

        ### Parameters

        - `scope`: The scope identifier

        ### Returns

        A bundle of ValueSets within the requested scope

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        parameters = {
            "scope": scope,
            "_summary": "true",
        }
        return self._get(
            path="/terminology/v1/fhir/r4/valueset",
            parameters=parameters,
        )

    def get_fhir_r4_value_set(
        self,
        value_set_id: str,
    ) -> GetFhirR4ValueSetResponse:
        """
        Retrieves a ValueSet by identifier

        ### Parameters

        - `value_set_id`: The ValueSet identifier

        ### Returns

        A ValueSet

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        return self._get(
            path=f"/terminology/v1/fhir/r4/valueset/{quote(value_set_id)}",
        )

    def summarize_fhir_r4_value_set(
        self,
        value_set_id: str,
    ) -> SummarizeFhirR4ValueSetResponse:
        """
        Summarizes the total number of codes in a ValueSet

        ### Parameters

        - `value_set_id`: The ValueSet identifier

        ### Returns

        A ValueSet resource with only the count populated

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        return self._get(
            path=f"/terminology/v1/fhir/r4/valueset/{quote(value_set_id)}",
            parameters={"_summary": "true"},
        )

    def get_fhir_r4_value_set_scopes(self) -> GetFhirR4ValueSetScopesResponse:
        """
        Requests the available ValueSet scopes

        ### Returns

        A unique ValueSet that contains a list of all scopes available on the server

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        return self._get(
            path="/terminology/v1/fhir/r4/valueset/Rosetta.ValueSetScopes",
        )

    def get_fhir_r4_value_sets_by_scope(
        self,
        name: Optional[str] = None,
        scope: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> GetFhirR4ValueSetsByScopeResponse:
        """
        Retrieves a paginated list of ValueSets filtered by name or scope

        ### Parameters

        - `name`: The name of the ValueSet
        - `scope`: Scope the ValueSet is in
        - `page_number`: When paginating, the page number to retrieve
        - `page_size`: When paginating, The page size to retrieve

        ### Returns

        A bundle of ValueSets that match the search criteria

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        parameters = {
            **_get_pagination_parameters(page_number, page_size),
            "name": name,
            "scope": scope,
        }
        return self._get(
            path=f"/terminology/v1/fhir/r4/valueset",
            parameters=parameters,
        )

    def summarize_fhir_r4_code_system(
        self, code_system: CodeSystems
    ) -> SummarizeFhirR4CodeSystemResponse:
        """
        Summarizes a code system, typically used to determine number of codes

        ### Parameters

        - `code_system`: The CodeSystem name to retrieve

        ### Returns

        An unpopulated CodeSystem

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/fhir/codesystem.html>
        """
        return self._get(
            path=f"/terminology/v1/fhir/r4/codesystem/{code_system}",
            parameters={"_summary": "true"},
        )

    def get_all_fhir_r4_value_sets_for_codes(
        self, parameters: Parameters
    ) -> GetAllFhirR4ValueSetsForCodesResponse:
        """
        In some situations it is useful to get the ValueSet(s) that a list of
        codes are members of. This can be used to categorize or group codes by
        ValueSet membership. For example, you may wish to:

        - Categorize a collection of NDC drug codes by their active ingredient.
        - Categorize a collection of LOINC lab tests by the component they are
          measuring.
        - Categorize a collection of ICD-10-CM Diagnoses into a broad set of
          disease groupings.

        ### Parameters

        - `parameters`: A Parameters resource containing at least one code, a system,
            and optionally a scope

        ### Returns

        A Parameters resource containing the classification results

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        return self._post(
            path="/terminology/v1/fhir/r4/valueset/$classify",
            body=parameters,
        )

    def convert_combined_fhir_r4_bundles(
        self,
        fhir_bundles: str,
        person_id: Optional[str] = None,
    ) -> ConvertCombinedFhirR4BundlesResponse:
        """
        This operation aggregates information retrieved from prior Convert API requests into a single entry.

        ### Parameters

        - `fhir_bundles`: A newline-delimited JSON list of FHIR R4 Bundles
        - `patient_id`: The patient ID to use for the FHIR bundle

        ### Returns

        A single FHIR R4 Bundle containing the merged data from the input.

        ### Documenation

        <https://rosetta-api.docs.careevolution.com/convert/combine_bundles.html>
        """
        headers = {"Content-Type": "application/x-ndjson"}
        route = _get_id_dependent_route("/convert/v1/combinefhirr4bundles", person_id)
        return self._post(
            path=route,
            body=fhir_bundles,
            headers=headers,
        )
