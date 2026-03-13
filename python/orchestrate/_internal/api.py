from typing import Optional

from orchestrate._internal.convert import ConvertApi
from orchestrate._internal.http_handler import HttpHandler, create_http_handler
from orchestrate._internal.insight import InsightApi
from orchestrate._internal.terminology import TerminologyApi


class OrchestrateApi:
    """
    Entry point for the Orchestrate Terminology, Convert, and Insight APIs.

    `OrchestrateApi` can be configured with constructor parameters or
    environment variables. When both are provided, constructor parameters take
    precedence over environment variables. For this client, `api_key` overrides
    `ORCHESTRATE_API_KEY`, `timeout_ms` overrides `ORCHESTRATE_TIMEOUT_MS`, and
    `ORCHESTRATE_BASE_URL` can be used to override the default base URL of
    `https://api.careevolutionapi.com`.

    The SDK also supports `ORCHESTRATE_ADDITIONAL_HEADERS` for adding headers to
    every request. The value must be a JSON object. These headers are merged in
    before the SDK's standard `Accept`, `Content-Type`, and authentication
    headers are applied, so SDK-managed headers take precedence on conflicts.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> None:
        """
        Creates a configured Orchestrate API client.

        ### Parameters

        - `api_key`: API key to send as the `x-api-key` header. If omitted, the
          client uses `ORCHESTRATE_API_KEY` when it is set.
        - `timeout_ms`: Request timeout in milliseconds. If omitted, the client
          uses `ORCHESTRATE_TIMEOUT_MS` when it is set, otherwise it defaults to
          `120000`.

        `ORCHESTRATE_BASE_URL` can be used to override the default API base URL
        without changing application code. When constructor parameters and
        environment variables both provide the same setting, the constructor
        parameter wins.
        """
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
