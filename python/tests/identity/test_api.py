from datetime import datetime, timedelta
from typing import Union
from uuid import uuid4

import pytest
from orchestrate._internal.identity.api import IdentityApi, Person, Record
from dotenv import load_dotenv

from orchestrate._internal.identity.demographic import Demographic
from orchestrate._internal.identity.local_hashing import (
    BlindedDemographic,
    HashDemographicResponse,
)

load_dotenv(override=True)

_TEST_API = IdentityApi()

_DEMOGRAPHIC = Demographic(
    first_name="John",
    last_name="Doe",
    dob="1980-01-01",
    gender="male",
)

_BLINDED_DEMOGRAPHIC = BlindedDemographic(
    data="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",
    version=1,
)

_DEFAULT_SOURCE = "source"


def _create_testing_record(identifier: str) -> Person:
    add_response = _TEST_API.add_or_update_record(
        source=_DEFAULT_SOURCE,
        identifier=identifier,
        first_name=_DEMOGRAPHIC.first_name,
        last_name=_DEMOGRAPHIC.last_name,
        dob=_DEMOGRAPHIC.dob,
        gender=_DEMOGRAPHIC.gender,
    )
    return add_response["matchedPerson"]


def _create_random_record() -> tuple[Person, str]:
    identifier = str(uuid4())
    return _create_testing_record(identifier), identifier


def test_constructor_should_build_from_passed_url():
    url = "http://localhost:8080"
    api = IdentityApi(url)

    assert api is not None
    assert api.__repr__() == f"IdentityApi(base_url={url!r})"


def test_add_or_update_record_should_add_record():
    response = _TEST_API.add_or_update_record(
        _DEFAULT_SOURCE,
        "identifier",
        first_name=_DEMOGRAPHIC.first_name,
        last_name=_DEMOGRAPHIC.last_name,
        dob=_DEMOGRAPHIC.dob,
        gender=_DEMOGRAPHIC.gender,
    )

    assert response is not None
    assert response["matchedPerson"]["id"] is not None


def test_add_or_update_record_with_demographic_should_add_record():
    response = _TEST_API.add_or_update_record(
        _DEFAULT_SOURCE,
        "identifier",
        _DEMOGRAPHIC,
    )

    assert response is not None
    assert response["matchedPerson"]["id"] is not None


def test_add_or_update_record_with_url_unsafe_identifier_should_add_record():
    response = _TEST_API.add_or_update_record(
        _DEFAULT_SOURCE,
        "id/entifier",
        first_name=_DEMOGRAPHIC.first_name,
        last_name=_DEMOGRAPHIC.last_name,
        dob=_DEMOGRAPHIC.dob,
        gender=_DEMOGRAPHIC.gender,
    )

    assert response is not None
    assert response["matchedPerson"]["id"] is not None


def test_add_or_update_blinded_record_should_add_record():
    response = _TEST_API.add_or_update_blinded_record(
        _DEFAULT_SOURCE,
        "identifier",
        data=_BLINDED_DEMOGRAPHIC["data"],
        version=_BLINDED_DEMOGRAPHIC["version"],
    )

    assert response is not None
    assert response["matchedPerson"]["id"] is not None


def test_add_or_update_blinded_record_with_kwargs_should_add_record():
    response = _TEST_API.add_or_update_blinded_record(
        source=_DEFAULT_SOURCE,
        identifier="identifier",
        data=_BLINDED_DEMOGRAPHIC["data"],
        version=_BLINDED_DEMOGRAPHIC["version"],
    )

    assert response is not None
    assert response["matchedPerson"]["id"] is not None


_ADD_OR_UPDATE_WITH_BLINDED_RECORD_DATA = [
    pytest.param(_BLINDED_DEMOGRAPHIC, id="blinded_demographic"),
    pytest.param(
        {
            "data": _BLINDED_DEMOGRAPHIC["data"],
            "version": _BLINDED_DEMOGRAPHIC["version"],
            "advisories": {"invalidDemographicFields": []},
        }
    ),
]


@pytest.mark.parametrize(
    ["demographic_request"], _ADD_OR_UPDATE_WITH_BLINDED_RECORD_DATA
)
def test_add_or_update_blinded_record_with_request_should_add_record(
    demographic_request: Union[BlindedDemographic, HashDemographicResponse]
) -> None:
    response = _TEST_API.add_or_update_blinded_record(
        _DEFAULT_SOURCE,
        "identifier",
        request=demographic_request,
    )

    assert response is not None
    assert response["matchedPerson"]["id"] is not None


def test_get_person_by_record_should_match() -> None:
    added_person, identifier = _create_random_record()

    response = _TEST_API.get_person_by_record(
        source=_DEFAULT_SOURCE, identifier=identifier
    )

    assert response is not None
    assert added_person["id"] == response["id"]


def test_get_person_by_id_should_match() -> None:
    added_person, _ = _create_random_record()

    response = _TEST_API.get_person_by_id(id_=added_person["id"])

    assert response is not None
    assert added_person["id"] == response["id"]


def test_match_demographics_with_demographic_should_match() -> None:
    response = _TEST_API.match_demographics(_DEMOGRAPHIC)

    assert response is not None
    assert "matchingPersons" in response


def test_match_demographics_with_demographic_kwarg_should_match() -> None:
    response = _TEST_API.match_demographics(demographic=_DEMOGRAPHIC)

    assert response is not None
    assert "matchingPersons" in response


def test_match_demographics_should_match() -> None:
    response = _TEST_API.match_demographics(
        first_name=_DEMOGRAPHIC.first_name,
        last_name=_DEMOGRAPHIC.last_name,
        dob=_DEMOGRAPHIC.dob,
        gender=_DEMOGRAPHIC.gender,
    )

    assert response is not None
    assert "matchingPersons" in response


def test_match_blinded_demographic_should_match() -> None:
    response = _TEST_API.match_blinded_demographics(
        data=_BLINDED_DEMOGRAPHIC["data"],
        version=_BLINDED_DEMOGRAPHIC["version"],
    )

    assert response is not None
    assert "matchingPersons" in response


def test_match_blinded_demographic_with_demographic_should_match() -> None:
    response = _TEST_API.match_blinded_demographics(_BLINDED_DEMOGRAPHIC)

    assert response is not None
    assert "matchingPersons" in response


def test_match_blinded_demographic_with_demographic_with_kwarg_should_match() -> None:
    response = _TEST_API.match_blinded_demographics(request=_BLINDED_DEMOGRAPHIC)

    assert response is not None
    assert "matchingPersons" in response


def test_delete_record_should_delete() -> None:
    added_person, identifier = _create_random_record()

    response = _TEST_API.delete_record(source=_DEFAULT_SOURCE, identifier=identifier)

    assert response is not None
    assert any(
        record["identifier"] == identifier and record["source"] == _DEFAULT_SOURCE
        for person in response["changedPersons"]
        for record in person["records"]
    )
    assert any(
        added_person["id"] == person["id"] for person in response["changedPersons"]
    )


def test_add_match_guidance_should_report_changed_persons() -> None:
    first_added_person, first_identifier = _create_random_record()
    second_added_person, second_identifier = _create_random_record()

    response = _TEST_API.add_match_guidance(
        record_one={"source": _DEFAULT_SOURCE, "identifier": first_identifier},
        record_two={"source": _DEFAULT_SOURCE, "identifier": second_identifier},
        action="Match",
        comment="Testing",
    )

    assert response is not None
    assert any(
        changed_person["id"] in [first_added_person["id"], second_added_person["id"]]
        for changed_person in response["changedPersons"]
    )


def test_remove_match_guidance_should_separate_persons() -> None:
    first_added_person, first_identifier = _create_random_record()
    second_added_person, second_identifier = _create_random_record()
    record_one: Record = {"source": _DEFAULT_SOURCE, "identifier": first_identifier}
    record_two: Record = {"source": _DEFAULT_SOURCE, "identifier": second_identifier}
    _TEST_API.add_match_guidance(
        record_one=record_one,
        record_two=record_two,
        action="Match",
        comment="Adding for removal testing",
    )

    response = _TEST_API.remove_match_guidance(
        record_one=record_one,
        record_two=record_two,
        comment="Removal testing",
    )

    assert response is not None
    assert any(
        changed_person["id"] in [first_added_person["id"], second_added_person["id"]]
        for changed_person in response["changedPersons"]
    )


def test_monitoring_identity_metrics_should_have_metrics():
    _create_random_record()

    response = _TEST_API.monitoring.identifier_metrics()

    assert response is not None
    assert "refreshed" in response
    assert response["totalRecordCount"] > 0
    assert response["totalPersonCount"] > 0
    assert response["globalMetricsRecords"] is not None
    assert response["globalMetricsRecords"][0]["source"] == ""
    assert response["summaryMetricsRecords"] is not None
    assert any(
        record["source"] == _DEFAULT_SOURCE
        for record in response["summaryMetricsRecords"]
    )
    assert response["sourceTotals"][0]["totalRecordCount"] > 0


def test_monitoring_overlap_metrics_should_have_metrics():
    _create_random_record()
    _create_random_record()

    response = _TEST_API.monitoring.overlap_metrics()

    assert response is not None
    assert response["datasourceOverlapRecords"] is not None
    assert any(
        record["datasourceA"] == _DEFAULT_SOURCE
        for record in response["datasourceOverlapRecords"]
    )
    assert any(
        record["datasourceB"] == _DEFAULT_SOURCE
        for record in response["datasourceOverlapRecords"]
    )
    assert response["datasourceOverlapRecords"][0]["overlapCount"] > 0
