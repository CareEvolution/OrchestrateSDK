from typing import Optional

from orchestrate._internal.convert import ConvertApi
from orchestrate._internal.http_handler import create_http_handler
from orchestrate._internal.insight import InsightApi
from orchestrate._internal.terminology import TerminologyApi


class OrchestrateApi:
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        additional_headers: Optional[dict] = None,
    ) -> None:
        self.__http_handler = create_http_handler(
            base_url=base_url,
            api_key=api_key,
            additional_headers=additional_headers,
        )

        self.terminology = TerminologyApi(self.__http_handler)
        self.convert = ConvertApi(self.__http_handler)
        self.insight = InsightApi(self.__http_handler)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(base_url={self.__http_handler.base_url!r})"
