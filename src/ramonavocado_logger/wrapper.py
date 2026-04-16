from functools import wraps

from .context_vars import _LOG_ENABLED

def toggle_log(enabled: bool = True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = _LOG_ENABLED.set(enabled)
            try:
                return func(*args, **kwargs)
            finally:
                _LOG_ENABLED.reset(token)

        return wrapper
    return decorator
