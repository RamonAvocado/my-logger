import logging
import structlog
from structlog.stdlib import BoundLogger

LEVEL3_STYLE = {
    "DEB": "\x1b[36m",  # cyan
    "INF": "\x1b[32m",  # green
    "WAR": "\x1b[33m",  # yellow
    "ERR": "\x1b[31m",  # red
    "CRI": "\x1b[35m",  # magenta
    "EXC": "\x1b[31m",  # red
}


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
            structlog.processors.add_log_level,
            level_rename,
            structlog.processors.TimeStamper(fmt="%H:%M:%S"),
            console_renderer,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


def get_log(**kwargs) -> BoundLogger:
    return structlog.get_logger(**kwargs)
