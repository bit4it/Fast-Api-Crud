from functools import wraps
from fastapi import Request, HTTPException
from app.core.config import settings

def x_api_key_required():
    """
    Decorator to check for a specific header key (and optionally value).
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request: Request = kwargs.get("request") or next(
                (a for a in args if isinstance(a, Request)), None
            )

            if not request:
                raise HTTPException(status_code=500, detail="Request object not found")

            # Check header
            api_key = request.headers.get("x-api-key")

            if not api_key:
                raise HTTPException(status_code=401, detail=f"Missing header: x-api-key")

            if api_key and api_key != settings.API_KEY:
                raise HTTPException(status_code=403, detail="Invalid API Key")

            return func(*args, **kwargs)
        return wrapper
    
    return decorator
