import json
from unittest.mock import Mock

import pytest
from requests import Response

from orchestrate.identity import (
    Demographic,
    IdentityApi,
    ValidateMatchNoMatchReason,
    ValidateMatchResponse,
)

pytestmark = pytest.mark.default


@pytest.mark.parametrize(
    "expected",
    [
        pytest.param(
            ValidateMatchResponse(
                result="NO_MATCH",
                noMatchReason=ValidateMatchNoMatchReason(
                    exactFields=["LastName"],
                    highSimilarityFields=["FirstName"],
                    lowSimilarityFields=["StreetName"],
                    differentFields=["DOB"],
                    recordAMissingFields=["Email"],
                    recordBMissingFields=["PhoneNumber"],
                ),
            ),
            id="all-comparison-categories",
        ),
        pytest.param(ValidateMatchResponse(result="NO_MATCH"), id="omitted-comparison"),
        pytest.param(
            ValidateMatchResponse(result="NO_MATCH", noMatchReason=None),
            id="null-comparison",
        ),
        pytest.param(
            ValidateMatchResponse(result="MATCH", matchReason="TestRule"),
            id="successful-match",
        ),
        pytest.param(
            ValidateMatchResponse(result="NO_MATCH", noMatchReason={}),
            id="empty-comparison",
        ),
        pytest.param(
            ValidateMatchResponse(
                result="NO_MATCH",
                noMatchReason={"exactFields": None, "recordAMissingFields": None},
            ),
            id="null-comparison-fields",
        ),
        pytest.param(
            ValidateMatchResponse(
                result="NO_MATCH", noMatchReason={"differentFields": ["DOB"]}
            ),
            id="partial-comparison",
        ),
    ],
)
def test_validate_match_should_send_demographics_and_return_response(
    monkeypatch: pytest.MonkeyPatch, expected: ValidateMatchResponse
) -> None:
    monkeypatch.delenv("ORCHESTRATE_IDENTITY_METRICS_KEY", raising=False)
    monkeypatch.delenv("ORCHESTRATE_ADDITIONAL_HEADERS", raising=False)
    http_response = Response()
    http_response.status_code = 200
    http_response.encoding = "utf-8"
    http_response._content = json.dumps(expected).encode("utf-8")
    post = Mock(return_value=http_response)
    monkeypatch.setattr("orchestrate._internal.http_handler.requests.post", post)
    api = IdentityApi(url="https://identity.example.test", api_key="test-api-key")

    response = api.validate_match(
        Demographic(first_name="SyntheticAlpha", home_phone_number="212-555-0175"),
        Demographic(first_name="SyntheticBeta", email="synthetic@example.test"),
    )

    assert response == expected
    post.assert_called_once()
    assert post.call_args.args[0] == "https://identity.example.test/v1/validateMatch"
    assert json.loads(post.call_args.kwargs["data"]) == [
        {"firstName": "SyntheticAlpha", "homePhoneNumber": "212-555-0175"},
        {"firstName": "SyntheticBeta", "email": "synthetic@example.test"},
    ]
