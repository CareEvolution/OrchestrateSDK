import os
import json
from typing import Any, Mapping, Optional

import requests


def _get_priority_base_url() -> str:
    if "ORCHESTRATE_BASE_URL" in os.environ:
        return os.environ["ORCHESTRATE_BASE_URL"]
    return "https://api.careevolutionapi.com"


def _get_priority_api_key(api_key: Optional[str]) -> Optional[str]:
    if api_key is not None:
        return api_key
    if "ORCHESTRATE_API_KEY" in os.environ:
        return os.environ["ORCHESTRATE_API_KEY"]
    return None


def _get_additional_headers() -> Mapping[str, str]:
    if "ORCHESTRATE_ADDITIONAL_HEADERS" in os.environ:
        return json.loads(os.environ["ORCHESTRATE_ADDITIONAL_HEADERS"])
    return {}


class HttpHandler:
    def __init__(
        self,
        base_url: str,
        default_headers: dict,
    ) -> None:
        self.base_url = base_url
        self.__default_headers = default_headers

    def __repr__(self) -> str:
        return f"HttpHandler(base_url={self.base_url})"

    def __merge_headers(self, headers: Optional[dict]) -> dict:
        if headers is None:
            return self.__default_headers
        return {**self.__default_headers, **headers}

    def post(
        self,
        path: str,
        body: Any,
        headers: Optional[dict[str, str]] = None,
        parameters: Optional[Mapping[str, Optional[str]]] = None,
    ) -> Any:
        request_headers = self.__merge_headers(headers)

        prepared_body = (
            json.dumps(body)
            if request_headers["Content-Type"] == "application/json"
            else body
        )
        url = f"{self.base_url}{path}"

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

    def get(
        self,
        path: str,
        headers: Optional[dict] = None,
        parameters: Optional[Mapping[str, Optional[str]]] = None,
    ) -> Any:
        request_headers = self.__merge_headers(headers)

        url = f"{self.base_url}{path}"
        response = requests.get(
            url,
            headers=request_headers,
            params=parameters,
        )
        response.raise_for_status()

        if (request_headers["Accept"] == "application/json") and response.text:
            return response.json()

        return response.text


def create_http_handler(api_key: Optional[str] = None) -> HttpHandler:
    additional_headers = _get_additional_headers()
    base_url = _get_priority_base_url()
    default_headers = {
        **(additional_headers or {}),
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    priority_api_key = _get_priority_api_key(api_key)
    if priority_api_key is not None:
        default_headers["x-api-key"] = priority_api_key

    return HttpHandler(
        base_url=base_url,
        default_headers=default_headers,
    )
