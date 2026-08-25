"""
OMNIS Logging Configuration.

This module configures the application's logging using structlog.
It provides a single entry point for logging setup and logger creation.
"""

from __future__ import annotations

import logging
import sys
from typing import cast

import structlog


def configure_logging() -> None:
    """
    Configure application logging.

    This function should be called exactly once during application startup.
    """

    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.INFO,
    )

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.dev.ConsoleRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )


def get_logger(name: str | None = None) -> structlog.stdlib.BoundLogger:
    """Return a configured logger."""
    return cast(structlog.stdlib.BoundLogger, structlog.get_logger(name))
