from omnis_api.core.logging import configure_logging, get_logger


def test_logger_creation() -> None:
    """Ensure the logger can be configured and used."""

    configure_logging()

    logger = get_logger(__name__)

    logger.info(
        "Logging initialized",
        version="0.1.0",
        environment="development",
    )

    assert logger is not None
