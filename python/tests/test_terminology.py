import pytest

from orchestrate._internal.terminology import (
    _build_translate_fhir_r4_concept_map_parameters,
)

pytestmark = [pytest.mark.default]


def _coding(parameters: dict) -> dict:
    return next(
        p["valueCoding"] for p in parameters["parameter"] if p["name"] == "coding"
    )


def _names(parameters: dict) -> list[str]:
    return [p["name"] for p in parameters["parameter"]]


def test_build_parameters_code_only():
    result = _build_translate_fhir_r4_concept_map_parameters(code="119981000146107")

    assert result["resourceType"] == "Parameters"
    assert _names(result) == ["coding"]
    assert _coding(result) == {"code": "119981000146107"}


def test_build_parameters_code_and_domain():
    result = _build_translate_fhir_r4_concept_map_parameters(
        code="119981000146107", domain="DiagnosisCode"
    )

    assert _names(result) == ["domain", "coding"]
    domain = next(p for p in result["parameter"] if p["name"] == "domain")
    assert domain["valueString"] == "DiagnosisCode"


def test_build_parameters_code_system_display():
    result = _build_translate_fhir_r4_concept_map_parameters(
        code="119981000146107",
        system="http://snomed.info/sct",
        display="Essential hypertension",
    )

    assert _coding(result) == {
        "system": "http://snomed.info/sct",
        "code": "119981000146107",
        "display": "Essential hypertension",
    }


def test_build_parameters_display_only():
    result = _build_translate_fhir_r4_concept_map_parameters(
        display="Essential hypertension"
    )

    assert _coding(result) == {"display": "Essential hypertension"}


def test_build_parameters_drops_empty_fields():
    result = _build_translate_fhir_r4_concept_map_parameters(
        code="119981000146107", system="", display=None
    )

    assert _coding(result) == {"code": "119981000146107"}
    assert _names(result) == ["coding"]
