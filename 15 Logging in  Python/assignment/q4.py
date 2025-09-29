### Assignment 4: Rotating Log Files

### 1. Write a Python function to create a logger that uses a rotating file handler, which creates a new log file 
###    when the current log file reaches a certain size.
### 2. Modify the function to keep a specified number of backup log files.
import logging
from logging.handlers import RotatingFileHandler

handler=RotatingFileHandler(
    'logs/q4.app.log',
    maxBytes=4*1024,
    backupCount=5
)
formatter=logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.debug("This is a message from Logger")
logger.info("This is a INFO message from Logger")
logger.error("This is an ERROR message from Logger")
logger.critical("This is a CRITICAL message from Logger")
logger.debug("This is a message from Logger")
logger.info("This is a INFO message from Logger")
logger.error("This is an ERROR message from Logger")
logger.critical("This is a CRITICAL message from Logger")
