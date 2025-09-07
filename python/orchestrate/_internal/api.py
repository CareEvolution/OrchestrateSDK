from typing import Optional

from orchestrate._internal.convert import ConvertApi
from orchestrate._internal.http_handler import HttpHandler, create_http_handler
from orchestrate._internal.insight import InsightApi
from orchestrate._internal.terminology import TerminologyApi


class OrchestrateApi:
    def __init__(
        self,
        api_key: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> None:
        self.__http_handler = create_http_handler(
            api_key=api_key, timeout_ms=timeout_ms
        )

        self.terminology = TerminologyApi(self.__http_handler)
        self.convert = ConvertApi(self.__http_handler)
        self.insight = InsightApi(self.__http_handler)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(base_url={self.__http_handler.base_url!r})"

    @property
    def _http_handler(self) -> HttpHandler:
        """
        Exposes the underlying HttpHandler instance for advanced usage. This is
        not part of the public API and may change without warning.
        """
        return self.__http_handler
