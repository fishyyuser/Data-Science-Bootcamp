### Assignment 7: Configuring Logging with a Dictionary

### 1. Write a Python function to configure logging using a dictionary. 
###    The configuration should include handlers for both file and console logging.

### 2. Modify the dictionary to include different logging levels and formats for each handler.

import logging
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "console_formatter": {
            "format": "%(asctime)s - console - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "file_formatter": {
            "format": "%(asctime)s - file - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "console_formatter",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "file_formatter",
            "filename": "logs/q7_app.log",
            "mode": "a"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"]
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()

logger.debug("This is a DEBUG message from the logger")
logger.info("This is an INFO message from the logger")
logger.error("This is an ERROR message from the logger")
