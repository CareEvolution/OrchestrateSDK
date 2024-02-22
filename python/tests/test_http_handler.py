from unittest.mock import Mock
from orchestrate._internal.http_handler import HttpHandler, create_http_handler


def test_api_base_url_in_environment_should_use_environment(monkeypatch):
    mock_http_handler = Mock(HttpHandler)
    monkeypatch.setattr(
        "orchestrate._internal.http_handler.HttpHandler", mock_http_handler
    )
    monkeypatch.setenv("ORCHESTRATE_BASE_URL", "test.api")

    handler = create_http_handler()

    assert handler is not None
    assert mock_http_handler.call_args[1]["base_url"] == "test.api"


def test_api_base_url_passed_should_prioritize(monkeypatch):
    mock_http_handler = Mock(HttpHandler)
    monkeypatch.setattr(
        "orchestrate._internal.http_handler.HttpHandler", mock_http_handler
    )
    monkeypatch.setenv("ORCHESTRATE_BASE_URL", "test.api")

    handler = create_http_handler("argument.api")

    assert handler is not None
    assert mock_http_handler.call_args[1]["base_url"] == "argument.api"


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
