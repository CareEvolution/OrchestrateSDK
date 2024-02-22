from io import BytesIO
import json
import os
from pathlib import Path
from unittest.mock import Mock
from zipfile import ZipFile

import pytest
from dotenv import load_dotenv
from orchestrate import OrchestrateApi
from requests import HTTPError
from orchestrate._internal.http_handler import HttpHandler, create_http_handler

from orchestrate.terminology import (
    ClassifyMedicationRequest,
    ClassifyObservationRequest,
    StandardizeRequest,
)


def setup_test_api():
    load_dotenv(Path(__file__).parent.parent.parent / ".env", override=True)
    api_key = os.environ.get("ORCHESTRATE_API_KEY", None)
    orchestrate_url = os.environ.get("ORCHESTRATE_BASE_URL", None)
    additional_headers_env = os.environ.get("ORCHESTRATE_ADDITIONAL_HEADERS", None)
    additional_headers = (
        json.loads(additional_headers_env) if additional_headers_env else None
    )

    return OrchestrateApi(
        api_key=api_key,
        base_url=orchestrate_url,
        additional_headers=additional_headers,
    )


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


_HL7 = """
MSH|^~\&|LAB|MYFAC|LAB||201411130917||ORU^R01|3216598|D|2.3|||AL|NE|
PID|1|ABC123DF|AND234DA_PID3|PID_4_ALTID|Smith^Patient^M||19670202 |F|||2222 22 st^^LAKE COUNTRY^NY^22222||222-222-2222|||||7890|
PV1|1|O|MYFACSOMPL||||^Smith^Patient^^^^^XAVS|||||||||||REF||SELF|||||||||||||||||||MYFAC||REG|||201411071440||||||||23390^PV1_52Smith^PV1_52Patient^H^^Dr^^PV1_52Mnemonic|
ORC|RE|PT103933301.0100|||CM|N|||201411130917|^John^Doctor^J.^^^^KYLA||^Smith^Patient^^^^^XAVS|MYFAC|
OBR|1|PT1311:H00001R301.0100|PT1311:H00001R|301.0100^Complete Blood Count (CBC)^00065227^57021-8^CBC \T\ Auto Differential^pCLOCD|R||201411130914|||KYLA||||201411130914||^Smith^Patient^^^^^XAVS||00065227||||201411130915||LAB|F||^^^^^R|^Smith^Patient^^^^^XAVS|
OBX|1|NM|301.0500^White Blood Count (WBC)^00065227^6690-2^Leukocytes^pCLOCD|1|10.1|10\S\9/L|3.1-9.7|H||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|2|NM|301.0600^Red Blood Count (RBC)^00065227^789-8^Erythrocytes^pCLOCD|1|3.2|10\S\12/L|3.7-5.0|L||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|3|NM|301.0700^Hemoglobin (HGB)^00065227^718-7^Hemoglobin^pCLOCD|1|140|g/L|118-151|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|4|NM|301.0900^Hematocrit (HCT)^00065227^4544-3^Hematocrit^pCLOCD|1|0.34|L/L|0.33-0.45|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|5|NM|301.1100^MCV^00065227^787-2^Mean Corpuscular Volume^pCLOCD|1|98.0|fL|84.0-98.0|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|6|NM|301.1300^MCH^00065227^785-6^Mean Corpuscular Hemoglobin^pCLOCD|1|27.0|pg|28.3-33.5|L||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|7|NM|301.1500^MCHC^00065227^786-4^Mean Corpuscular Hemoglobin Concentration^pCLOCD|1|330|g/L|329-352|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|8|NM|301.1700^RDW^00065227^788-0^Erythrocyte Distribution Width^pCLOCD|1|12.0|%|12.0-15.0|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|9|NM|301.1900^Platelets^00065227^777-3^Platelets^pCLOCD|1|125|10\S\9/L|147-375|L||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|10|NM|301.2100^Neutrophils^00065227^751-8^Neutrophils^pCLOCD|1|8.0|10\S\9/L|1.2-6.0|H||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|11|NM|301.2300^Lymphocytes^00065227^731-0^Lymphocytes^pCLOCD|1|1.0|10\S\9/L|0.6-3.1|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|12|NM|301.2500^Monocytes^00065227^742-7^Monocytes^pCLOCD|1|1.0|10\S\9/L|0.1-0.9|H||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|13|NM|301.2700^Eosinophils^00065227^711-2^Eosinophils^pCLOCD|1|0.0|10\S\9/L|0.0-0.5|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|14|NM|301.2900^Basophils^00065227^704-7^Basophils^pCLOCD|1|0.0|10\S\9/L|0.0-0.2|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
ZDR||^Smith^Patient^^^^^XAVS^^^^^XX^^ATP|
ZPR||
"""


def test_api_convert_hl7_to_fhir_r4_without_patient_should_convert():
    result = TEST_API.convert.hl7_to_fhir_r4(content=_HL7)

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_api_convert_hl7_to_fhir_r4_with_patient_should_convert():
    result = TEST_API.convert.hl7_to_fhir_r4(content=_HL7, patient_id="1234")

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


_CDA = """
<?xml-stylesheet type="text/xsl" href=""?>
<ClinicalDocument xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 cda.xsd" moodCode="EVN" xmlns="urn:hl7-org:v3">
  <realmCode code="US" />
  <typeId root="2.16.840.1.113883.1.3" extension="POCD_HD000040" />
  <templateId root="2.16.840.1.113883.10" extension="IMPL_CDAR2_LEVEL1" />
  <templateId root="2.16.840.1.113883.10.20.22.1.1" />
  <templateId root="2.16.840.1.113883.10.20.22.1.2" />
  <id root="3d1e9964-5fbd-4180-85af-0d473e3b43ec" />
  <code code="34133-9" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="Summary of Episode Note" />
  <title>Medical Summary Document</title>
  <effectiveTime value="20150205121815-0500" />
  <confidentialityCode code="N" codeSystem="2.16.840.1.113883.5.25" codeSystemName="HL7 Confidentiality Code" displayName="Normal" />
  <languageCode code="en-US" />
  <recordTarget typeCode="RCT" contextControlCode="OP">
    <patientRole classCode="PAT">
      <id root="1.3.6.1.4.1.37608" extension="IheTestPatient" />
      <addr>
        <streetAddressLine>34 Drury Lane</streetAddressLine>
        <city>Disney Land</city>
        <state>CA</state>
        <postalCode>90210</postalCode>
      </addr>
      <telecom value="534-555-6666" use="HP" />
      <patient classCode="PSN" determinerCode="INSTANCE">
        <name>
          <given>Patient</given>
          <family>Smith</family>
        </name>
        <administrativeGenderCode code="F" codeSystem="DemoNamespace" codeSystemName="DemoNamespace" displayName="Female" />
        <birthTime value="19560813000000-0400" />
        <maritalStatusCode nullFlavor="UNK" />
        <raceCode nullFlavor="UNK" />
        <ethnicGroupCode nullFlavor="UNK" />
      </patient>
    </patientRole>
  </recordTarget>
  <component>
    <structuredBody>
      <component>
        <section classCode="DOCSECT" moodCode="EVN">
          <templateId root="2.16.840.1.113883.10.20.22.2.4.1" />
          <templateId root="2.16.840.1.113883.10.20.22.2.4" />
          <id root="175b3e57-db29-43e4-8158-e785594c9845" />
          <code code="8716-3" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="Vital Signs" />
          <title>Vital Signs</title>
          <text mediaType="text/x-hl7-text+xml">No Vital Signs Available</text>
          <entry>
            <organizer classCode="CLUSTER" moodCode="EVN">
              <templateId root="2.16.840.1.113883.10.20.22.4.26" />
              <id nullFlavor="UNK" />
              <code code="46680005" codeSystem="2.16.840.1.113883.6.96" codeSystemName="SNOMED CT" displayName="Vital signs" />
              <statusCode code="completed" />
              <effectiveTime nullFlavor="UNK" />
              <component>
                <observation classCode="OBS" moodCode="EVN" negationInd="true">
                  <templateId root="2.16.840.1.113883.10.20.22.4.27" />
                  <id nullFlavor="UNK" />
                  <code nullFlavor="UNK" />
                  <statusCode code="completed" />
                  <effectiveTime nullFlavor="UNK" />
                  <value xsi:type="PQ" nullFlavor="NI" />
                </observation>
              </component>
            </organizer>
          </entry>
        </section>
      </component>
    </structuredBody>
  </component>
</ClinicalDocument>
"""


def test_convert_cda_to_fhir_r4_without_patient_should_convert():
    result = TEST_API.convert.cda_to_fhir_r4(content=_CDA)

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_convert_cda_to_fhir_r4_with_patient_should_convert():
    result = TEST_API.convert.cda_to_fhir_r4(content=_CDA, patient_id="1234")

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
    result = TEST_API.convert.cda_to_pdf(content=_CDA)

    assert result is not None
    assert isinstance(result, bytes)
    #  Check for PDF magic number
    assert [int(byte) for byte in result[0:5]] == [37, 80, 68, 70, 45]


_BUNDLE = {
    "resourceType": "Bundle",
    "type": "batch-response",
    "entry": [
        {
            "fullUrl": "https://api.careevolutionapi.com/Patient/35b77437-425d-419c-90b5-af4bc433ebe9",
            "resource": {
                "resourceType": "Patient",
                "id": "35b77437-425d-419c-90b5-af4bc433ebe9",
                "meta": {
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608"
                },
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MR",
                                }
                            ]
                        },
                        "system": "urn:oid:1.3.6.1.4.1.37608",
                        "value": "IheTestPatient",
                    },
                    {
                        "system": "http://rosetta.careevolution.com/identifiers/Proprietary/1.3.6.1.4.1.37608",
                        "value": "IheTestPatient",
                    },
                ],
                "name": [{"use": "official", "family": "Smith", "given": ["Patient"]}],
                "telecom": [
                    {"system": "phone", "value": "534-555-6666", "use": "home"}
                ],
                "gender": "female",
                "birthDate": "1956-08-13",
                "deceasedBoolean": False,
                "address": [
                    {
                        "use": "home",
                        "line": ["34 Drury Lane"],
                        "city": "Disney Land",
                        "state": "CA",
                        "postalCode": "90210",
                    }
                ],
            },
        }
    ],
}


def test_convert_fhir_r4_to_cda_should_convert():
    result = TEST_API.convert.fhir_r4_to_cda(content=_BUNDLE)

    assert result is not None
    assert result.startswith("<?xml")


def test_convert_fhir_r4_to_omop_should_convert():
    result = TEST_API.convert.fhir_r4_to_omop(content=_BUNDLE)

    assert result is not None
    assert isinstance(result, bytes)
    with ZipFile(BytesIO(result)) as zip_file:
        assert len(zip_file.infolist()) > 0


_RISK_PROFILE_BUNDLE = {
    "resourceType": "Bundle",
    "type": "searchset",
    "entry": [
        {
            "resource": {
                "resourceType": "Patient",
                "id": "9cee689b-6501-4349-af32-e6849e179a2f",
                "meta": {
                    "lastUpdated": "2023-02-22T11:27:29.9499804+00:00",
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient",
                        "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-Patient",
                    ],
                },
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/patient-religion",
                        "valueCodeableConcept": {
                            "coding": [
                                {
                                    "system": "urn:oid:1.2.3.4.5.1.1",
                                    "code": "Example",
                                    "display": "Example",
                                    "userSelected": True,
                                }
                            ]
                        },
                    },
                    {
                        "extension": [{"url": "text", "valueString": "N"}],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                    },
                    {
                        "extension": [
                            {"url": "text", "valueString": "Black"},
                            {
                                "url": "detailed",
                                "valueCoding": {
                                    "system": "urn:oid:2.16.840.1.113883.6.238",
                                    "code": "2056-0",
                                    "display": "BLACK",
                                    "userSelected": False,
                                },
                            },
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
                    },
                ],
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MR",
                                }
                            ]
                        },
                        "system": "http://test.careevolution.com/identifiers/CareEvolution/MRN/1.2.3.4.5.1.7_1.2.3.4.5.1.7",
                        "value": "0i56756845575l8yw6u886k4",
                    },
                    {
                        "system": "http://test.careevolution.com/identifiers/1.2.3.4.5.1.7/1.2.3.4.5.1.7",
                        "value": "0i56756845575l8yw6u886k4",
                    },
                    {
                        "system": "http://test.careevolution.com/identifiers/1.2.3.4.5.1.7/1.3.6.1.4.1.5641",
                        "value": "46274464",
                    },
                ],
                "name": [
                    {
                        "use": "official",
                        "_use": {
                            "extension": [
                                {
                                    "url": "http://careevolution.com/fhirextensions#term",
                                    "valueCodeableConcept": {
                                        "coding": [
                                            {
                                                "system": "http://careevolution.com/fhircodes#NameType",
                                                "code": "LegalName",
                                                "display": "Legal Name",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                }
                            ]
                        },
                        "family": "Tester",
                        "given": ["Brittany"],
                    },
                    {
                        "_use": {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                                    "valueCode": "unsupported",
                                },
                                {
                                    "url": "http://careevolution.com/fhirextensions#term",
                                    "valueCodeableConcept": {
                                        "coding": [
                                            {
                                                "system": "http://careevolution.com/fhircodes#NameType",
                                                "code": "P",
                                                "display": "Pseudonym",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                },
                            ]
                        },
                        "family": "Tester",
                        "given": ["Brittany"],
                    },
                ],
                "telecom": [
                    {
                        "system": "phone",
                        "_system": {
                            "extension": [
                                {
                                    "url": "http://careevolution.com/fhirextensions#term",
                                    "valueCodeableConcept": {
                                        "coding": [
                                            {
                                                "system": "http://careevolution.com/fhircodes#ContactInfoType",
                                                "code": "HomePhone",
                                                "display": "Home Phone",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                }
                            ]
                        },
                        "value": "tel:(680)555-1234",
                        "use": "home",
                        "_use": {
                            "extension": [
                                {
                                    "url": "http://careevolution.com/fhirextensions#term",
                                    "valueCodeableConcept": {
                                        "coding": [
                                            {
                                                "system": "urn:oid:1.2.3.4.5.1.7",
                                                "code": "HP",
                                                "display": "primary home",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                }
                            ]
                        },
                    },
                    {
                        "system": "phone",
                        "_system": {
                            "extension": [
                                {
                                    "url": "http://careevolution.com/fhirextensions#term",
                                    "valueCodeableConcept": {
                                        "coding": [
                                            {
                                                "system": "http://careevolution.com/fhircodes#ContactInfoType",
                                                "code": "OfficePhone",
                                                "display": "Office Phone",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                }
                            ]
                        },
                        "value": "tel:(548)555-8765",
                        "use": "work",
                        "_use": {
                            "extension": [
                                {
                                    "url": "http://careevolution.com/fhirextensions#term",
                                    "valueCodeableConcept": {
                                        "coding": [
                                            {
                                                "system": "urn:oid:1.2.3.4.5.1.7",
                                                "code": "WP",
                                                "display": "work place",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                }
                            ]
                        },
                    },
                    {
                        "_system": {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                                    "valueCode": "unsupported",
                                },
                                {
                                    "url": "http://careevolution.com/fhirextensions#term",
                                    "valueCodeableConcept": {
                                        "coding": [
                                            {
                                                "system": "urn:oid:1.2.3.4.5.1.7",
                                                "code": "MC",
                                                "display": "mobile contact",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                },
                            ]
                        },
                        "value": "tel:(574)555-3737",
                    },
                    {
                        "_system": {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                                    "valueCode": "unsupported",
                                },
                                {
                                    "url": "http://careevolution.com/fhirextensions#term",
                                    "valueCodeableConcept": {
                                        "coding": [
                                            {
                                                "system": "urn:oid:1.2.3.4.5.1.7",
                                                "code": "Other",
                                                "display": "Other",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                },
                            ]
                        },
                        "value": "tel:(189)555-333",
                    },
                ],
                "gender": "male",
                "_gender": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "urn:oid:2.16.840.1.113883.5.1",
                                        "code": "M",
                                        "display": "Male",
                                        "userSelected": True,
                                    },
                                    {
                                        "system": "http://careevolution.com",
                                        "code": "M",
                                        "display": "Male",
                                        "userSelected": False,
                                    },
                                    {
                                        "system": "http://test.careevolution.com/codes/FhirCodesAlternate1/Gender",
                                        "code": "M",
                                        "display": "M",
                                        "userSelected": False,
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/v3/AdministrativeGender",
                                        "code": "M",
                                        "display": "Male",
                                        "userSelected": False,
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/administrative-gender",
                                        "code": "male",
                                        "display": "male",
                                        "userSelected": False,
                                    },
                                    {
                                        "system": "http://test.careevolution.com/codes/FhirCodes/Gender",
                                        "code": "male",
                                        "userSelected": False,
                                    },
                                ]
                            },
                        }
                    ]
                },
                "birthDate": "1948-12-17",
                "deceasedBoolean": False,
                "address": [
                    {
                        "use": "home",
                        "line": ["2608 Main Street"],
                        "city": "Anytown",
                        "state": "MI",
                        "postalCode": "48761",
                    }
                ],
                "maritalStatus": {
                    "coding": [
                        {
                            "system": "urn:oid:1.2.3.4.5.1.1",
                            "code": "M",
                            "display": "M",
                            "userSelected": True,
                        }
                    ]
                },
                "communication": [
                    {
                        "language": {
                            "coding": [
                                {
                                    "system": "urn:oid:1.2.3.4.5.1.7",
                                    "code": "ENGLISH",
                                    "display": "ENGLISH",
                                    "userSelected": True,
                                }
                            ]
                        },
                        "preferred": True,
                    }
                ],
            }
        }
    ],
}


def test_insight_risk_profile_should_return_bundle():
    result = TEST_API.insight.risk_profile(
        content=_RISK_PROFILE_BUNDLE,  # type: ignore
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
            json.dumps(_BUNDLE),
            json.dumps(_BUNDLE),
        ]
    )

    result = TEST_API.convert.combine_fhir_r4_bundles(content=bundles)

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) == 2


def test_convert_combined_fhir_r4_bundles_with_person_should_combine():
    bundles = "\n".join(
        [
            json.dumps(_BUNDLE),
            json.dumps(_BUNDLE),
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


_X12_DOCUMENT = """ISA*00*          *00*          *ZZ*SUBMITTERID    *ZZ*RECEIVERID     *230616*1145*^*00501*000000001*0*T*:~
GS*HC*SENDERCODE*RECEIVERCODE*20230627*11301505*123456789*X*005010X222A1~
ST*837*0034*005010X223A1~
BHT*0019*00*3920394930203*20100816*1615*CH~
NM1*41*2*HOWDEE HOSPITAL*****46*0123456789~
PER*IC*BETTY RUBBLE*TE*9195551111~
NM1*40*2*BCBSNC*****46*987654321~
HL*1**20*1~
NM1*85*2*HOWDEE HOSPITAL*****XX*1245011012~
N3*123 HOWDEE BLVD~
N4*DURHAM*NC*27701~
REF*EI*123456789~
PER*IC*WILMA RUBBLE*TE*9195551111*FX*6145551212~
HL*2*1*22*0~
SBR*P*18*XYZ1234567******BL~
NM1*IL*1*DOUGH*MARY****MI*24672148306~
N3*BOX 12312~
N4*DURHAM*NC*27715~
DMG*D8*19670807*F~
NM1*PR*2*BCBSNC*****PI*987654321~
CLM*2235057*200***13:A:1***A**Y*Y~
DTP*434*RD8*20100730-20100730~
CL1*1*9*01~
REF*F8*ASD0000123~
HI*BK:25000~
HI*BF:78901~
HI*BR:4491:D8:20100730~
HI*BH:41:D8:20100501*BH:27:D8:20100715*BH:33:D8:20100415*BH:C2:D8:20100410~
HI*BE:30:::20~
HI*BG:01~
NM1*71*1*SMITH*ELIZABETH*AL***34*243898989~
REF*1G*P97777~
LX*1~
SV2*0300*HC:81000*120*UN*1~
DTP*472*D8*20100730~
LX*2~
SV2*0320*HC:76092*50*UN*1~
DTP*472*D8*20100730~
LX*3~
SV2*0270*HC:J1120*30*UN*1~
DTP*472*D8*20100730~
SE*38*0034~
GE*1*30~
IEA*1*000000031~
"""


def test_convert_x12_to_fhir_r4_should_return_a_bundle():
    result = TEST_API.convert.x12_to_fhir_r4(content=_X12_DOCUMENT)

    assert result is not None
    assert result["resourceType"] == "Bundle"
    assert len(result["entry"]) > 0


def test_convert_x12_to_fhir_r4_with_patient_should_return_a_bundle():
    result = TEST_API.convert.x12_to_fhir_r4(content=_X12_DOCUMENT, patient_id="12/34")

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
    with pytest.raises(HTTPError):
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
