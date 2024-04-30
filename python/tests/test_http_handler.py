from typing import Any
from unittest.mock import Mock

import pytest
from orchestrate._internal.exceptions import OrchestrateClientError
from orchestrate._internal.http_handler import HttpHandler, create_http_handler
from dotenv import dotenv_values

pytestmark = [pytest.mark.e2e, pytest.mark.default]


def test_api_base_url_in_environment_should_use_environment(monkeypatch):
    mock_http_handler = Mock(HttpHandler)
    monkeypatch.setattr(
        "orchestrate._internal.http_handler.HttpHandler", mock_http_handler
    )
    monkeypatch.setenv("ORCHESTRATE_BASE_URL", "test.api")

    handler = create_http_handler()

    assert handler is not None
    assert mock_http_handler.call_args[1]["base_url"] == "test.api"


def test_api_base_url_unconfigured_should_default(monkeypatch):
    mock_http_handler = Mock(HttpHandler)
    monkeypatch.setattr(
        "orchestrate._internal.http_handler.HttpHandler", mock_http_handler
    )

    handler = create_http_handler()

    assert handler is not None
    assert (
        mock_http_handler.call_args[1]["base_url"] == "https://api.careevolutionapi.com"
    )


def test_api_api_key_in_environment_should_use_environment(monkeypatch):
    mock_http_handler = Mock(HttpHandler)
    monkeypatch.setattr(
        "orchestrate._internal.http_handler.HttpHandler", mock_http_handler
    )
    monkeypatch.setenv("ORCHESTRATE_API_KEY", "api-key")

    handler = create_http_handler()

    assert handler is not None
    assert mock_http_handler.call_args[1]["default_headers"]["x-api-key"] == "api-key"


def test_api_api_key_not_supplied_should_not_include_in_default_headers(monkeypatch):
    mock_http_handler = Mock(HttpHandler)
    monkeypatch.setattr(
        "orchestrate._internal.http_handler.HttpHandler", mock_http_handler
    )
    monkeypatch.delenv("ORCHESTRATE_API_KEY", raising=False)

    handler = create_http_handler()

    assert handler is not None
    assert "x-api-key" not in mock_http_handler.call_args[1]["default_headers"]


def test_api_api_key_passed_should_prioritize(monkeypatch):
    mock_http_handler = Mock(HttpHandler)
    monkeypatch.setattr(
        "orchestrate._internal.http_handler.HttpHandler", mock_http_handler
    )
    monkeypatch.setenv("ORCHESTRATE_API_KEY", "api-key")

    handler = create_http_handler(api_key="argument-api-key")

    assert handler is not None
    assert (
        mock_http_handler.call_args[1]["default_headers"]["x-api-key"]
        == "argument-api-key"
    )


_OUTCOME_POST_TEST_DATA = [
    pytest.param(
        "application/json",
        "application/json",
        "/convert/v1/fhirstu3tofhirr4",
        {"resourceType": "Patient"},
        "Expected a Bundle but found a Patient",
        id="json",
    ),
    pytest.param(
        "application/json",
        "application/xml",
        "/convert/v1/fhirstu3tofhirr4",
        {"resourceType": "Patient"},
        "Expected a Bundle but found a Patient",
        id="xml",
    ),
    pytest.param(
        "application/xml",
        "text/html",
        "/convert/v1/cdatohtml",
        "<ClinicalDocument></ClinicalDocument>",
        "CDA did not render",
        id="html",
    ),
    pytest.param(
        "application/xml",
        "application/pdf",
        "/convert/v1/cdatopdf",
        "<ClinicalDocument></ClinicalDocument>",
        "CDA did not render",
        id="pdf",
    ),
    pytest.param(
        "application/json",
        "application/zip",
        "/convert/v1/fhirr4toomop",
        {"resourceType": "Patient"},
        "Expected a Bundle but found a Patient",
        id="zip",
    ),
]


@pytest.mark.parametrize(
    argnames=["content_type", "accept_header", "route", "payload", "expected_message"],
    argvalues=_OUTCOME_POST_TEST_DATA,
)
def test_http_handler_post_bad_request_should_throw_orchestrate_error(
    content_type: str,
    accept_header: str,
    route: str,
    payload: Any,
    expected_message: str,
):
    config = dotenv_values()
    handler = HttpHandler(
        "https://api.careevolutionapi.com",
        {
            "x-api-key": config["ORCHESTRATE_API_KEY"],
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    with pytest.raises(OrchestrateClientError) as exc_info:
        handler.post(
            route, payload, {"Accept": accept_header, "Content-Type": content_type}
        )

    assert expected_message in str(exc_info.value)
