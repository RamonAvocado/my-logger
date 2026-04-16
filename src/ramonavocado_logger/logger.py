import logging
import structlog

## PROCESSORS ##
from structlog.processors import CallsiteParameterAdder, CallsiteParameter, TimeStamper

from structlog.stdlib import BoundLogger

from .context_vars import _LOG_ENABLED

LEVEL3_STYLE = {
    "DEB": "\x1b[36m",  # cyan
    "INF": "\x1b[32m",  # green
    "WAR": "\x1b[33m",  # yellow
    "ERR": "\x1b[31m",  # red
    "CRI": "\x1b[35m",  # magenta
    "EXC": "\x1b[31m",  # red
}


def callsite(_, __, event_dict):
    if not event_dict.pop("location", False):
        return event_dict

    return CallsiteParameterAdder(
        [
            CallsiteParameter.PATHNAME,
            CallsiteParameter.FUNC_NAME,
            CallsiteParameter.LINENO,
        ]
    )(_, __, event_dict)


def drop_if_disabled(_, __, event_dict):
    if not _LOG_ENABLED.get():
        raise structlog.DropEvent
    return event_dict


def level_rename(_, __, event_dict):
    level = event_dict.get("level")
    if level:
        event_dict["level"] = level[:3].upper()
    return event_dict


def configure_logging(level=logging.INFO):
    logging.basicConfig(
        format="%(message)s",
        level=level,
    )
    console_renderer = structlog.dev.ConsoleRenderer(
        pad_level=False,
        level_styles=LEVEL3_STYLE,
    )

    structlog.configure(
        processors=[
            drop_if_disabled,
            structlog.processors.add_log_level,
            callsite,
            level_rename,
            TimeStamper(fmt="%H:%M:%S"),
            console_renderer,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


def get_log(**kwargs) -> BoundLogger:
    return structlog.get_logger(**kwargs)
