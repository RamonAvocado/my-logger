import contextvars

_LOG_ENABLED = contextvars.ContextVar("_LOG_ENABLED", default=True)
