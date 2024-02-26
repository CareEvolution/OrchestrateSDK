import json
from typing import Any, Mapping, Optional

import requests


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
