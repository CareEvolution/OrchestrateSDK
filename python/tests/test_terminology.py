from unittest.mock import Mock

import pytest

from orchestrate._internal.terminology import (
    _build_translate_fhir_r4_concept_map_parameters,
    TerminologyApi,
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


def test_build_parameters_treats_whitespace_only_fields_as_absent():
    result = _build_translate_fhir_r4_concept_map_parameters(
        code="119981000146107", system="   "
    )

    assert _coding(result) == {"code": "119981000146107"}


def test_build_parameters_omits_domain_when_whitespace_only():
    result = _build_translate_fhir_r4_concept_map_parameters(
        code="119981000146107", domain="   "
    )

    assert _names(result) == ["coding"]


def test_build_parameters_omits_coding_when_all_fields_absent():
    result = _build_translate_fhir_r4_concept_map_parameters(system="  ")

    assert result["parameter"] == []


PAGED_ROUTES = [
    (
        "get_fhir_r4_code_system",
        {"code_system": "LOINC", "concept_contains": "blood pressure"},
        "/codesystem/LOINC",
        "concept",
        {"concept:contains": "blood pressure"},
    ),
    (
        "summarize_fhir_r4_code_systems",
        {},
        "/codesystem",
        "entry",
        {"_summary": "true"},
    ),
    ("get_fhir_r4_concept_maps", {}, "/conceptmap", "entry", {}),
    (
        "get_fhir_r4_value_sets_by_scope",
        {"name": "test name", "scope": "http://loinc.org"},
        "/valueset",
        "entry",
        {"name": "test name", "extension.scope": "http://loinc.org"},
    ),
    (
        "summarize_fhir_r4_value_set_scope",
        {"scope": "http://loinc.org"},
        "/valueset",
        "entry",
        {"_summary": "true", "extension.scope": "http://loinc.org"},
    ),
]


EXPLICIT_ROUTES = [
    route
    for route in PAGED_ROUTES
    if route[0]
    in (
        "get_fhir_r4_code_system",
        "get_fhir_r4_concept_maps",
        "get_fhir_r4_value_sets_by_scope",
    )
]
BUNDLE_ROUTES = [route for route in PAGED_ROUTES if route[3] == "entry"]


@pytest.fixture
def paging_handler():
    return Mock()


@pytest.fixture
def terminology(paging_handler):
    return TerminologyApi(paging_handler)


@pytest.mark.parametrize("method,arguments,path,field,filters", EXPLICIT_ROUTES)
@pytest.mark.parametrize("page_number", [0, 3])
def test_explicit_paging_should_return_only_requested_page(
    terminology, paging_handler, method, arguments, path, field, filters, page_number
):
    response = {
        "resourceType": "CodeSystem" if field == "concept" else "Bundle",
        field: [{"id": "one"}],
        "link": [{"relation": "next", "url": "/unused"}],
    }
    paging_handler.get.return_value = response
    result = getattr(terminology, method)(
        **arguments, page_number=page_number, page_size=2
    )
    assert result is response
    assert result["link"] == [{"relation": "next", "url": "/unused"}]
    paging_handler.get.assert_called_once_with(
        path=f"/terminology/v1/fhir/r4{path}",
        parameters={**filters, "page.num": str(page_number), "_count": "2"},
    )


@pytest.mark.parametrize("method,arguments,path,field,filters", EXPLICIT_ROUTES)
@pytest.mark.parametrize("paging", [{"page_number": 0}, {"page_size": 2}])
def test_incomplete_paging_should_fail_before_http(
    terminology, paging_handler, method, arguments, path, field, filters, paging
):
    with pytest.raises(
        ValueError, match="page_number and page_size must be provided together"
    ):
        getattr(terminology, method)(**arguments, **paging)
    paging_handler.get.assert_not_called()


@pytest.mark.parametrize("method,arguments,path,field,filters", BUNDLE_ROUTES)
@pytest.mark.parametrize(
    "next_link",
    ["/continuation?cursor=a%2Bb", "https://example.test/continuation?cursor=a%2Bb"],
)
def test_bundle_should_follow_next_links_regardless_of_total_or_empty_page(
    terminology, paging_handler, method, arguments, path, field, filters, next_link
):
    first = {
        "resourceType": "Bundle",
        "id": "resource-id",
        "total": 0,
        "link": [
            {"relation": "next", "url": next_link},
            {"relation": "alternate", "url": "/catalog"},
        ],
    }
    paging_handler.get.side_effect = [
        first,
        {
            "entry": [{"id": "one"}],
            "link": [{"relation": "next", "url": "?cursor=last%2Ftoken"}],
        },
        {"entry": [{"id": "two"}]},
    ]
    result = getattr(terminology, method)(**arguments)
    assert result == {
        "resourceType": "Bundle",
        "id": "resource-id",
        "total": 0,
        "entry": [{"id": "one"}, {"id": "two"}],
        "link": [{"relation": "alternate", "url": "/catalog"}],
    }
    assert paging_handler.get.call_count == 3
    calls = paging_handler.get.call_args_list
    assert calls[0].kwargs == {
        "path": f"/terminology/v1/fhir/r4{path}",
        "parameters": {**filters, "page.num": "0", "_count": "10000"},
    }
    assert calls[1].kwargs == {"path": next_link}
    assert calls[2].kwargs == {
        "path": ("https://example.test" if next_link.startswith("https:") else "")
        + "/continuation?cursor=last%2Ftoken"
    }


@pytest.mark.parametrize("method,arguments,path,field,filters", BUNDLE_ROUTES)
def test_bundle_without_next_link_should_stop_even_if_total_suggests_more(
    terminology, paging_handler, method, arguments, path, field, filters
):
    paging_handler.get.return_value = {"entry": [{"id": "one"}], "total": 999}
    assert getattr(terminology, method)(**arguments) == {
        "entry": [{"id": "one"}],
        "total": 999,
    }
    assert paging_handler.get.call_count == 1


@pytest.mark.parametrize("known_count", [False, True])
def test_code_system_should_aggregate_concepts_with_numbered_pages(
    terminology, paging_handler, known_count
):
    first = {
        "resourceType": "CodeSystem",
        "concept": [{"code": "one"}],
        **({"count": 2} if known_count else {}),
    }
    paging_handler.get.side_effect = [first, {"concept": [{"code": "two"}]}, {}]
    result = terminology.get_fhir_r4_code_system(
        "LOINC", concept_contains="blood pressure"
    )
    assert result == {**first, "concept": [{"code": "one"}, {"code": "two"}]}
    assert paging_handler.get.call_count == (2 if known_count else 3)
    for index, call in enumerate(paging_handler.get.call_args_list):
        assert call.kwargs == {
            "path": "/terminology/v1/fhir/r4/codesystem/LOINC",
            "parameters": {
                "concept:contains": "blood pressure",
                "page.num": str(index),
                "_count": "10000",
            },
        }


@pytest.mark.parametrize("method,arguments,path,field,filters", PAGED_ROUTES)
def test_automatic_paging_should_stop_on_empty_first_page(
    terminology, paging_handler, method, arguments, path, field, filters
):
    response = {field: []}
    paging_handler.get.return_value = response
    assert getattr(terminology, method)(**arguments) is response
    assert paging_handler.get.call_count == 1


@pytest.mark.parametrize("method,arguments,path,field,filters", PAGED_ROUTES)
def test_automatic_paging_should_propagate_later_failure(
    terminology, paging_handler, method, arguments, path, field, filters
):
    paging_handler.get.side_effect = [
        {field: [{"id": "one"}], "link": [{"relation": "next", "url": "/next"}]},
        RuntimeError("page failed"),
    ]
    with pytest.raises(RuntimeError, match="page failed"):
        getattr(terminology, method)(**arguments)
    assert paging_handler.get.call_count == 2
