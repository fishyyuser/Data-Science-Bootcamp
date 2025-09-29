### Assignment 10: Advanced Logging Configuration

### 1. Write a Python function to configure logging using an external configuration file (e.g., `logging.conf`).
#      The configuration should include handlers for file and console logging.
### 2. Modify the configuration file to use different logging levels and formats for each handler.

import logging
import logging.config

logging.config.fileConfig("logging.conf")

logger = logging.getLogger("Q10")

logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")