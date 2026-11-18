import os
import secrets

from fastapi import Request
from starlette.responses import JSONResponse

async def api_authenticate_key(request: Request, call_next):
    # Keep browser pages usable and let local development requests work without
    # needing a secret header. Set ENFORCE_API_KEY=true to require it.
    if request.method == "OPTIONS" or request.url.path in {
        "/",
        "/docs",
        "/redoc",
        "/openapi.json",
    }:
        return await call_next(request)

    if os.getenv("ENFORCE_API_KEY", "false").strip().lower() not in {"1", "true", "yes"}:
        return await call_next(request)

    api_key = request.headers.get("X-API-KEY", "")
    expected_key = os.getenv("AUTHENTICATED_KEY", "")

    if (
        not expected_key
        or not api_key
        or not secrets.compare_digest(api_key, expected_key)
    ):
        return JSONResponse(
            status_code=403,
            content={"message": "Unauthorized Request"},
        )

    return await call_next(request)

