from io import BytesIO
import json
import os
from pathlib import Path
from zipfile import ZipFile

import pytest
from dotenv import load_dotenv
from orchestrate import OrchestrateApi
from requests import HTTPError

from orchestrate._internal.exceptions import (
    OrchestrateClientError,
    OrchestrateHttpError,
)
from .data import (
    CDA,
    DSTU2_BUNDLE,
    HL7,
    NEMSIS_BUNDLE,
    R4_BUNDLE,
    RISK_PROFILE_BUNDLE,
    STU3_BUNDLE,
    X12_DOCUMENT,
)

from orchestrate.terminology import (
    ClassifyMedicationRequest,
    ClassifyObservationRequest,
    StandardizeRequest,
)


def setup_test_api():
    load_dotenv(Path(__file__).parent.parent.parent / ".env", override=True)
    return OrchestrateApi()


TEST_API = setup_test_api()


@pytest.mark.parametrize(
    "condition",
    [
        pytest.param(
            {"code": "119981000146107", "system": "http://snomed.info/sct"},
            id="expanded-uri",
        ),
        pytest.param(
            {"code": "119981000146107", "system": "SNOMED"}, id="expanded-name"
        ),
        pytest.param(
            {
                "request": {
                    "code": "119981000146107",
                    "system": "http://snomed.info/sct",
                }
            },
            id="request-uri",
        ),
        pytest.param(
            {"request": {"code": "119981000146107", "system": "SNOMED"}},
            id="request-name",
        ),
        pytest.param(
            {
                "request": [
                    {"code": "119981000146107", "system": "http://snomed.info/sct"},
                    {"code": "119981000146107", "system": "SNOMED"},
                ]
            },
            id="batch",
        ),
    ],
)
def test_api_classify_condition_should_classify(condition):
    kwarg_response = TEST_API.terminology.classify_condition(**condition)
    positional_response = TEST_API.terminology.classify_condition(
        *[condition[key] for key in condition]
    )

    response = kwarg_response
    assert kwarg_response == positional_response
    assert response is not None
    if isinstance(response, list):
        assert len(response) == 2
        assert [item["cciAcute"] for item in response]
    else:
        assert response["cciAcute"]


@pytest.mark.parametrize(
    "medication",
    [
        pytest.param(
            {
                "code": "2468231",
                "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
            },
            id="expanded-uri",
        ),
        pytest.param({"code": "2468231", "system": "RxNorm"}, id="expanded-name"),
        pytest.param(
            {
                "request": {
                    "code": "2468231",
                    "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                }
            },
            id="request-uri",
        ),
        pytest.param(
            {"request": {"code": "2468231", "system": "RxNorm"}},
            id="request-name",
        ),
    ],
)
def test_api_classify_medication_should_classify(medication):
    kwarg_response = TEST_API.terminology.classify_medication(**medication)
    positional_response = TEST_API.terminology.classify_medication(
        *[medication[key] for key in medication]
    )

    response = kwarg_response
    assert kwarg_response == positional_response
    assert response is not None
    assert response["rxNormGeneric"]


def test_api_classify_medication_should_classify_batch() -> None:
    request: list[ClassifyMedicationRequest] = [
        {
            "code": "2468231",
            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
        },
        {"code": "2468231", "system": "RxNorm"},
    ]

    response = TEST_API.terminology.classify_medication(request=request)
    positional_response = TEST_API.terminology.classify_medication(request)

    assert response == positional_response
    assert response is not None
    assert len(response) == 2
    assert [item["rxNormGeneric"] for item in response]


@pytest.mark.parametrize(
    "observation",
    [
        pytest.param(
            {
                "code": "94558-4",
                "system": "http://loinc.org",
            },
            id="expanded-uri",
        ),
        pytest.param({"code": "94558-4", "system": "LOINC"}, id="expanded-name"),
        pytest.param(
            {
                "request": {
                    "code": "94558-4",
                    "system": "http://loinc.org",
                }
            },
            id="request-uri",
        ),
        pytest.param(
            {"request": {"code": "94558-4", "system": "LOINC"}},
            id="request-name",
        ),
    ],
)
def test_api_classify_observation_should_classify(observation):
    kwarg_response = TEST_API.terminology.classify_observation(**observation)
    positional_response = TEST_API.terminology.classify_observation(
        *[observation[key] for key in observation]
    )

    response = kwarg_response
    assert kwarg_response == positional_response
    assert response is not None
    assert response["loincClass"] == "MICRO"


def test_api_classify_observation_should_classify_batch() -> None:
    requests: list[ClassifyObservationRequest] = [
        {
            "code": "94558-4",
            "system": "http://loinc.org",
        },
        {"code": "94558-4", "system": "LOINC"},
    ]

    kwarg_response = TEST_API.terminology.classify_observation(request=requests)
    positional_response = TEST_API.terminology.classify_observation(requests)

    response = kwarg_response
    assert kwarg_response == positional_response
    assert response is not None
    assert len(response) == 2
    assert [item["loincClass"] == "MICRO" for item in response]


_STANDARDIZE_CONDITION_PAYLOADS = [
    pytest.param({"code": "370221004"}, "370221004", id="snomed"),
    pytest.param({"request": {"code": "370221004"}}, "370221004", id="snomed-request"),
    pytest.param({"code": "J45.50"}, "J45.50", id="icd"),
    pytest.param({"request": {"code": "J45.50"}}, "J45.50", id="icd-request"),
    pytest.param({"display": "dm2"}, "44054006", id="display"),
    pytest.param({"request": {"display": "dm2"}}, "44054006", id="display-request"),
]


@pytest.mark.parametrize("payload, expected", _STANDARDIZE_CONDITION_PAYLOADS)
def test_api_standardize_condition_should_standardize(payload, expected):
    response = TEST_API.terminology.standardize_condition(**payload)
    positional_response = TEST_API.terminology.standardize_condition(
        *[payload[key] for key in payload]
    )

    assert response == positional_response
    assert response is not None
    assert any(coding["code"] == expected for coding in response["coding"])


def test_api_standardize_condition_should_standardize_batch() -> None:
    requests: list[StandardizeRequest] = [
        {"code": "370221004"},
        {"code": "J45.50"},
        {"display": "dm2"},
    ]
    expected = ["370221004", "J45.50", "44054006"]
    response = TEST_API.terminology.standardize_condition(request=requests)
    positional_response = TEST_API.terminology.standardize_condition(requests)

    assert response == positional_response
    assert response is not None
    assert len(response) == 3
    assert any(coding["code"] == expected[0] for coding in response[0]["coding"])
    assert any(coding["code"] == expected[1] for coding in response[1]["coding"])
    assert any(coding["code"] == expected[2] for coding in response[2]["coding"])


_STANDARDIZE_LAB_PAYLOADS = [
    pytest.param({"code": "4548-4"}, "4548-4", id="loinc"),
    pytest.param({"request": {"code": "4548-4"}}, "4548-4", id="loinc-request"),
    pytest.param(
        {"display": "hba1c 1/15/22 from outside lab"}, "43396009", id="display"
    ),
    pytest.param(
        {"request": {"display": "hba1c 1/15/22 from outside lab"}},
        "43396009",
        id="display-request",
    ),
]


@pytest.mark.parametrize("payload, expected", _STANDARDIZE_LAB_PAYLOADS)
def test_api_standardize_lab_should_standardize(payload, expected):
    response = TEST_API.terminology.standardize_lab(**payload)
    positional_response = TEST_API.terminology.standardize_lab(
        *[payload[key] for key in payload]
    )

    assert response == positional_response
    assert response is not None
    assert any(coding["code"] == expected for coding in response["coding"])


def test_api_standardize_lab_should_standardize_batch() -> None:
    requests: list[StandardizeRequest] = [
        {"code": "4548-4"},
        {"display": "hba1c 1/15/22 from outside lab"},
    ]
    expected = ["4548-4", "43396009"]

    response = TEST_API.terminology.standardize_lab(request=requests)
    positional_response = TEST_API.terminology.standardize_lab(requests)

    assert response == positional_response
    assert response is not None
    assert len(response) == 2
    assert any(coding["code"] == expected[0] for coding in response[0]["coding"])
    assert any(coding["code"] == expected[1] for coding in response[1]["coding"])


_STANDARDIZE_MEDICATION_PAYOADS = [
    pytest.param({"code": "861004", "system": "RxNorm"}, "861004", id="rxnorm"),
    pytest.param(
        {"request": {"code": "861004", "system": "RxNorm"}},
        "861004",
        id="rxnorm-request",
    ),
    pytest.param({"code": "59267-1000-02"}, "59267100002", id="ndc"),
    pytest.param(
        {"request": {"code": "59267-1000-02"}}, "59267100002", id="ndc-request"
    ),
    pytest.param(
        {"display": "Jentadueto extended (linagliptin 2.5 / metFORMIN  1000mg)"},
        "1796093",
        id="display",
    ),
    pytest.param(
        {
            "request": {
                "display": "Jentadueto extended (linagliptin 2.5 / metFORMIN  1000mg)"
            }
        },
        "1796093",
        id="display-request",
    ),
]


@pytest.mark.parametrize("payload, expected", _STANDARDIZE_MEDICATION_PAYOADS)
def test_api_standardize_medication_should_standardize(payload, expected):
    response = TEST_API.terminology.standardize_medication(**payload)
    positional_response = TEST_API.terminology.standardize_medication(
        *[payload[key] for key in payload]
    )

    assert response == positional_response
    assert response is not None
    assert any(coding["code"] == expected for coding in response["coding"])


def test_api_standardize_medication_should_standardize_batch() -> None:
    requests: list[StandardizeRequest] = [
        {"code": "861004", "system": "RxNorm"},
        {"code": "59267-1000-02"},
        {"display": "Jentadueto extended (linagliptin 2.5 / metFORMIN  1000mg)"},
    ]
    expected = ["861004", "59267100002", "1796093"]

    response = TEST_API.terminology.standardize_medication(request=requests)
    positional_response = TEST_API.terminology.standardize_medication(requests)

    assert response == positional_response
    assert response is not None
    assert len(response) == 3
    assert any(coding["code"] == expected[0] for coding in response[0]["coding"])
    assert any(coding["code"] == expected[1] for coding in response[1]["coding"])
    assert any(coding["code"] == expected[2] for coding in response[2]["coding"])


_STANDARDIZE_OBSERVATION_PAYLOADS = [
    pytest.param({"code": "8480-6"}, "8480-6", id="loinc"),
    pytest.param({"request": {"code": "8480-6"}}, "8480-6", id="loinc-request"),
    pytest.param({"display": "BMI"}, "39156-5", id="display"),
    pytest.param({"request": {"display": "BMI"}}, "39156-5", id="display-request"),
]


@pytest.mark.parametrize("payload, expected", _STANDARDIZE_OBSERVATION_PAYLOADS)
def test_api_standardize_observation_should_standardize(payload, expected):
    response = TEST_API.terminology.standardize_observation(**payload)
    positional_response = TEST_API.terminology.standardize_observation(
        *[payload[key] for key in payload]
    )

    assert response == positional_response
    assert response is not None
    assert any(coding["code"] == expected for coding in response["coding"])


def test_api_standardize_observation_should_standardize_batch() -> None:
    requests: list[StandardizeRequest] = [{"code": "8480-6"}, {"display": "BMI"}]
    expected = ["8480-6", "39156-5"]

    response = TEST_API.terminology.standardize_observation(request=requests)
    positional_response = TEST_API.terminology.standardize_observation(requests)

    assert response == positional_response
    assert response is not None
    assert len(response) == 2
    assert any(coding["code"] == expected[0] for coding in response[0]["coding"])
    assert any(coding["code"] == expected[1] for coding in response[1]["coding"])


_STANDARDIZE_PROCEDURE_PAYLOADS = [
    pytest.param({"code": "80146002"}, "80146002", id="snomed"),
    pytest.param({"request": {"code": "80146002"}}, "80146002", id="snomed-request"),
    pytest.param({"display": "ct head&neck"}, "429858000", id="display"),
    pytest.param({"request": {"display": "ct head&neck"}}, "429858000", id="display"),
]


@pytest.mark.parametrize("payload, expected", _STANDARDIZE_PROCEDURE_PAYLOADS)
def test_api_standardize_procedure_should_standardize(payload, expected):
    response = TEST_API.terminology.standardize_procedure(**payload)
    positional_response = TEST_API.terminology.standardize_procedure(
        *[payload[key] for key in payload]
    )

    assert response == positional_response
    assert response is not None
    assert any(coding["code"] == expected for coding in response["coding"])


def test_api_standardize_procedure_should_standardize_batch() -> None:
    requests: list[StandardizeRequest] = [
        {"code": "80146002"},
        {"display": "ct head&neck"},
    ]
    expected = ["80146002", "429858000"]

    response = TEST_API.terminology.standardize_procedure(request=requests)
    positional_response = TEST_API.terminology.standardize_procedure(requests)

    assert response == positional_response
    assert response is not None
    assert len(response) == 2
    assert any(coding["code"] == expected[0] for coding in response[0]["coding"])
    assert any(coding["code"] == expected[1] for coding in response[1]["coding"])


_STANDARDIZE_RADIOLOGY_PAYLOADS = [
    pytest.param({"code": "711232001", "system": "SNOMED"}, "711232001", id="snomed"),
    pytest.param(
        {"request": {"code": "711232001", "system": "SNOMED"}},
        "711232001",
        id="snomed-request",
    ),
    pytest.param(
        {"display": "CT scan of head w/o iv contrast 3d ago@StJoes"},
        "30799-1",
        id="display",
    ),
    pytest.param(
        {"request": {"display": "CT scan of head w/o iv contrast 3d ago@StJoes"}},
        "30799-1",
        id="display-request",
    ),
]


@pytest.mark.parametrize("payload, expected", _STANDARDIZE_RADIOLOGY_PAYLOADS)
def test_api_standardize_radiology_should_standardize(payload, expected):
    response = TEST_API.terminology.standardize_radiology(**payload)
    positional_response = TEST_API.terminology.standardize_radiology(
        *[payload[key] for key in payload]
    )

    assert response == positional_response
    assert response is not None
    assert any(coding["code"] == expected for coding in response["coding"])


def test_api_standardize_radiology_should_standardize_batch() -> None:
    requests: list[StandardizeRequest] = [
        {"code": "711232001", "system": "SNOMED"},
        {"display": "CT scan of head w/o iv contrast 3d ago@StJoes"},
    ]
    expected = ["711232001", "30799-1"]

    response = TEST_API.terminology.standardize_radiology(request=requests)
    positional_response = TEST_API.terminology.standardize_radiology(requests)

    assert response == positional_response
    assert response is not None
    assert len(response) == 2
    assert any(coding["code"] == expected[0] for coding in response[0]["coding"])
    assert any(coding["code"] == expected[1] for coding in response[1]["coding"])


def test_api_convert_hl7_to_fhir_r4_without_patient_should_convert():
    result = TEST_API.convert.hl7_to_fhir_r4(content=HL7)

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_api_convert_hl7_to_fhir_r4_with_patient_should_convert():
    result = TEST_API.convert.hl7_to_fhir_r4(content=HL7, patient_id="1234")

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0
    patient_resource = next(
        (
            entry["resource"]
            for entry in result["entry"]
            if entry["resource"]["resourceType"] == "Patient"
        )
    )
    assert patient_resource["id"] == "1234"


def test_convert_cda_to_fhir_r4_without_patient_should_convert():
    result = TEST_API.convert.cda_to_fhir_r4(content=CDA)

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_convert_cda_to_fhir_r4_with_patient_should_convert():
    result = TEST_API.convert.cda_to_fhir_r4(content=CDA, patient_id="1234")

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0
    patient_resource = next(
        (
            entry["resource"]
            for entry in result["entry"]
            if entry["resource"]["resourceType"] == "Patient"
        )
    )
    assert patient_resource["id"] == "1234"


def test_convert_cda_to_pdf_should_convert():
    result = TEST_API.convert.cda_to_pdf(content=CDA)

    assert result is not None
    assert isinstance(result, bytes)
    #  Check for PDF magic number
    assert [int(byte) for byte in result[0:5]] == [37, 80, 68, 70, 45]


def test_convert_fhir_r4_to_cda_should_convert():
    result = TEST_API.convert.fhir_r4_to_cda(content=R4_BUNDLE)

    assert result is not None
    assert result.startswith("<?xml")


def test_convert_fhir_r4_to_omop_should_convert():
    result = TEST_API.convert.fhir_r4_to_omop(content=R4_BUNDLE)

    assert result is not None
    assert isinstance(result, bytes)
    with ZipFile(BytesIO(result)) as zip_file:
        assert len(zip_file.infolist()) > 0


def test_insight_risk_profile_should_return_bundle():
    result = TEST_API.insight.risk_profile(
        content=RISK_PROFILE_BUNDLE,  # type: ignore
        hcc_version="22",
        period_end_date="2020-12-31",
        ra_segment="community nondual aged",
    )

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_convert_combined_fhir_r4_bundles_should_combine():
    bundles = "\n".join(
        [
            json.dumps(R4_BUNDLE),
            json.dumps(R4_BUNDLE),
        ]
    )

    result = TEST_API.convert.combine_fhir_r4_bundles(content=bundles)

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) == 2


def test_convert_combined_fhir_r4_bundles_with_person_should_combine():
    bundles = "\n".join(
        [
            json.dumps(R4_BUNDLE),
            json.dumps(R4_BUNDLE),
        ]
    )

    result = TEST_API.convert.combine_fhir_r4_bundles(
        content=bundles, patient_id="1234"
    )

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) == 2
    patient_resource = next(
        (
            entry["resource"]
            for entry in result["entry"]
            if entry["resource"]["resourceType"] == "Patient"
        )
    )
    assert patient_resource["id"] == "1234"


def test_convert_x12_to_fhir_r4_should_return_a_bundle():
    result = TEST_API.convert.x12_to_fhir_r4(content=X12_DOCUMENT)

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_convert_x12_to_fhir_r4_with_patient_should_return_a_bundle():
    result = TEST_API.convert.x12_to_fhir_r4(content=X12_DOCUMENT, patient_id="12/34")

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0
    patient_resource = next(
        (
            entry["resource"]
            for entry in result["entry"]
            if entry["resource"]["resourceType"] == "Patient"
        )
    )
    assert patient_resource["id"] == "12/34"


def test_get_fhir_r4_code_system_should_return_a_code_system():
    result = TEST_API.terminology.get_fhir_r4_code_system(code_system="SNOMED")

    assert result is not None
    assert result["resourceType"] == "CodeSystem"
    assert len(result["concept"]) > 0


def test_get_fhir_r4_code_system_with_page_should_return_a_code_system():
    result = TEST_API.terminology.get_fhir_r4_code_system(
        code_system="SNOMED",
        page_number=0,
        page_size=2,
    )

    assert result is not None
    assert result["resourceType"] == "CodeSystem"
    assert len(result["concept"]) > 0


def test_get_fhir_r4_code_system_with_search_should_return_a_code_system():
    result = TEST_API.terminology.get_fhir_r4_code_system(
        code_system="SNOMED",
        concept_contains="myocardial infarction",
        page_number=0,
        page_size=2,
    )

    assert result is not None
    assert result["resourceType"] == "CodeSystem"
    assert len(result["concept"]) > 0


def test_summarize_fhir_r4_code_systems_should_return_bundle():
    result = TEST_API.terminology.summarize_fhir_r4_code_systems()

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_get_fhir_r4_concept_maps_should_return_a_bundle():
    result = TEST_API.terminology.get_fhir_r4_concept_maps()

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_translate_fhir_r4_concept_map_with_code_should_translate():
    result = TEST_API.terminology.translate_fhir_r4_concept_map(code="119981000146107")

    assert result is not None
    assert result["resourceType"] == "Parameters"
    assert len(result["parameter"]) > 0


def test_translate_fhir_r4_concept_map_with_code_and_domain_should_translate():
    result = TEST_API.terminology.translate_fhir_r4_concept_map(
        code="119981000146107", domain="Condition"
    )

    assert result is not None
    assert result["resourceType"] == "Parameters"
    assert len(result["parameter"]) > 0


def test_summarize_fhir_r4_value_set_scope_should_return_bundle():
    result = TEST_API.terminology.summarize_fhir_r4_value_set_scope(
        scope="http://loinc.org"
    )

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0
    assert len(result["entry"]) <= 10000


def test_get_fhir_r4_value_set_should_return_a_value_set():
    result = TEST_API.terminology.get_fhir_r4_value_set(
        value_set_id="00987FA2EDADBD0E43DA59E171B80F99DBF832C69904489EE6F9E6450925E5A2"
    )

    assert result is not None
    assert result["resourceType"] == "ValueSet"
    assert len(result["compose"]["include"]) > 0


def test_summarize_fhir_r4_value_set_should_return_a_value_set():
    result = TEST_API.terminology.summarize_fhir_r4_value_set(
        value_set_id="00987FA2EDADBD0E43DA59E171B80F99DBF832C69904489EE6F9E6450925E5A2"
    )

    assert result is not None
    assert result["resourceType"] == "ValueSet"


def test_get_fhir_r4_value_set_scopes_should_return_value_set():
    result = TEST_API.terminology.get_fhir_r4_value_set_scopes()

    assert result is not None
    assert result["resourceType"] == "ValueSet"
    assert len(result["compose"]["include"]) > 0


def test_get_fhir_r4_value_sets_by_scope_no_pagination_should_raise():
    with pytest.raises(OrchestrateHttpError):
        TEST_API.terminology.get_fhir_r4_value_sets_by_scope(scope="http://loinc.org")


def test_get_fhir_r4_value_seets_by_scope_with_page_and_scope_should_return_bundle():
    result = TEST_API.terminology.get_fhir_r4_value_sets_by_scope(
        scope="http://loinc.org", page_number=0, page_size=2
    )

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_get_fhir_r4_value_seets_by_scope_with_page_and_name_should_return_bundle():
    result = TEST_API.terminology.get_fhir_r4_value_sets_by_scope(
        name="LP7839-6", page_number=0, page_size=2
    )

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_get_fhir_r4_value_seets_by_scope_with_page_and_name_and_scope_should_return_bundle():
    result = TEST_API.terminology.get_fhir_r4_value_sets_by_scope(
        name="LP7839-6", scope="http://loinc.org", page_number=0, page_size=2
    )

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_get_fhir_r4_value_seets_by_scope_with_page_should_return_bundle():
    result = TEST_API.terminology.get_fhir_r4_value_sets_by_scope(
        page_number=0, page_size=2
    )

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_summarize_fhir_r4_code_system_should_return_code_system():
    result = TEST_API.terminology.summarize_fhir_r4_code_system(code_system="SNOMED")

    assert result is not None
    assert result["resourceType"] == "CodeSystem"
    assert result["count"] > 0


def test_get_all_fhir_r4_value_sets_for_codes_should_return_parameters():
    parameters = {
        "resourceType": "Parameters",
        "parameter": [
            {"name": "code", "valueString": "119981000146107"},
            {"name": "system", "valueString": "http://snomed.info/sct"},
        ],
    }
    result = TEST_API.terminology.get_all_fhir_r4_value_sets_for_codes(parameters)

    assert result is not None
    assert result["resourceType"] == "Parameters"
    assert len(result["parameter"]) > 0


def test_convert_fhir_dstu2_to_fhir_r4_should_convert():
    result = TEST_API.convert.fhir_dstu2_to_fhir_r4(content=DSTU2_BUNDLE)

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0
    patient_resource = next(
        (
            entry["resource"]
            for entry in result["entry"]
            if entry["resource"]["resourceType"] == "Patient"
        )
    )
    assert any(
        identifier["value"] == "12345A" and identifier["id"] == "id3"
        for identifier in patient_resource["identifier"]
    )


def test_convert_fhir_stu3_to_fhir_r4_should_convert():
    result = TEST_API.convert.fhir_stu3_to_fhir_r4(content=STU3_BUNDLE)

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0
    patient_resource = next(
        (
            entry["resource"]
            for entry in result["entry"]
            if entry["resource"]["resourceType"] == "Patient"
        )
    )
    assert any(
        identifier["value"] == "1234A" and identifier["id"] == "id3"
        for identifier in patient_resource["identifier"]
    )


def test_convert_fhir_r4_to_health_lake_should_convert():
    result = TEST_API.convert.fhir_r4_to_health_lake(content=R4_BUNDLE)

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert result["type"] == "collection"
    assert result["entry"][0]["resource"]["resourceType"] == "Bundle"
    assert result["entry"][0]["resource"]["type"] == "batch"


def test_convert_cda_to_html_should_convert():
    result = TEST_API.convert.cda_to_html(content=CDA)

    assert result is not None
    assert result.startswith("<html")


def test_convert_cda_to_fhir_r4_alternative_encoding_should_send_bytes():
    file = Path(__file__).parent / "data" / "encoding_cda.xml"

    result = TEST_API.convert.cda_to_fhir_r4(content=file.read_text())

    assert result is not None
    assert result["resourceType"] == "Bundle"


def test_convert_fhir_r4_to_nemsis_v34_should_convert():
    result = TEST_API.convert.fhir_r4_to_nemsis_v34(content=NEMSIS_BUNDLE)

    assert result is not None
    assert "<EMSDataSet" in result
    assert "<eOutcome.18" not in result


def test_convert_fhir_r4_to_nemsis_v35_should_convert():
    result = TEST_API.convert.fhir_r4_to_nemsis_v35(content=NEMSIS_BUNDLE)

    assert result is not None
    assert "<EMSDataSet" in result
    assert "<eOutcome.18" in result
