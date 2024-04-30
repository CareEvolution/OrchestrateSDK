from pathlib import Path
from orchestrate._internal.identity.demographic import Demographic
from orchestrate._internal.identity.local_hashing import LocalHashingApi
from dotenv import load_dotenv

import pytest

pytestmark = pytest.mark.e2e


load_dotenv(Path(__file__).parent.parent.parent.parent / ".env", override=True)
_TEST_API = LocalHashingApi()

_DEMOGRAPHIC = Demographic(
    first_name="John",
    last_name="Doe",
    dob="1980-01-01",
    gender="male",
)


def test_hash_should_hash_by_keyword():
    response = _TEST_API.hash_(
        first_name=_DEMOGRAPHIC.first_name,
        last_name=_DEMOGRAPHIC.last_name,
        dob=_DEMOGRAPHIC.dob,
        gender=_DEMOGRAPHIC.gender,
    )

    assert response is not None
    assert response["version"] > 0
    assert response["advisories"]["invalidDemographicFields"] == []


def test_hash_with_invalid_demographics_should_return_advisories():
    response = _TEST_API.hash_(
        first_name=_DEMOGRAPHIC.first_name,
        last_name=_DEMOGRAPHIC.last_name,
        dob="121980-01-01",
    )

    assert response is not None
    assert response["advisories"]["invalidDemographicFields"] == ["dob"]


def test_hash_should_hash_by_demographic():
    response = _TEST_API.hash_(_DEMOGRAPHIC)

    assert response is not None
    assert response["version"] > 0
    assert response["advisories"]["invalidDemographicFields"] == []


def test_constructor_should_build_from_passed_url():
    url = "http://localhost:8080"
    api = LocalHashingApi(url)

    assert api is not None
    assert api.__repr__() == f"LocalHashingApi(base_url={url!r})"
