from .logger import configure_logging, get_log
from .wrapper import toggle_log

configure_logging()

__all__ = ["get_log", "toggle_log"]
