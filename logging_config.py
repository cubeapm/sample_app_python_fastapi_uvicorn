import logging
from json_log_formatter import JSONFormatter

def configure_logging():
    log_handler = logging.StreamHandler()

    formatter = JSONFormatter()

    log_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(log_handler)

    logging.getLogger("uvicorn.access").handlers = [log_handler]
    logging.getLogger("uvicorn.error").handlers = [log_handler]
