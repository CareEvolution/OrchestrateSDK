from typing import Any, Callable, Optional

from orchestrate._internal.http_handler import HttpHandler


def _get_coding_body(
    code: Optional[str] = None,
    system: Optional[str] = None,
    display: Optional[str] = None,
) -> dict[str, str]:
    body = {}
    if code is not None:
        body["code"] = code
    if system is not None:
        body["system"] = system
    if display is not None:
        body["display"] = display

    return body


def handle_batch_overloaded_request(
    http_handler: HttpHandler, *args, **kwargs
) -> Callable[[str], Any]:
    body: dict[str, Any] = {}
    request = kwargs.get("request")
    if request is None and len(args) > 0:
        request = args[0]
    if isinstance(request, list):
        body = {"items": [_get_coding_body(**item) for item in request]}
        return lambda url: http_handler.post(f"{url}/batch", body).get("items")
    if isinstance(request, dict):
        body = _get_coding_body(**request)
        return lambda url: http_handler.post(url, body)

    code = kwargs.get("code") or (args[0] if len(args) > 0 else None)
    system = kwargs.get("system") or (args[1] if len(args) > 1 else None)
    display = kwargs.get("display") or (args[2] if len(args) > 2 else None)
    body = _get_coding_body(code, system, display)
    return lambda url: http_handler.post(url, body)
