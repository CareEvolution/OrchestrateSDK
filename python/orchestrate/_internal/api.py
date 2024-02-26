from typing import Optional

from orchestrate._internal.convert import ConvertApi
from orchestrate._internal.http_handler import HttpHandler
from orchestrate._internal.insight import InsightApi
from orchestrate._internal.terminology import TerminologyApi


class OrchestrateApi:
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        additional_headers: Optional[dict] = None,
    ) -> None:
        default_headers = {
            **(additional_headers or {}),
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if api_key is not None:
            default_headers["x-api-key"] = api_key

        self.__http_handler = HttpHandler(
            base_url=base_url or "https://api.careevolutionapi.com",
            default_headers=default_headers,
        )
        self.terminology = TerminologyApi(self.__http_handler)
        self.convert = ConvertApi(self.__http_handler)
        self.insight = InsightApi(self.__http_handler)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(base_url={self.__http_handler.base_url!r})"
