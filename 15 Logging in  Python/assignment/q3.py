### Assignment 3: Formatting Log Messages

### 1. Write a Python function to create a logger with a custom log message format 
###   that includes the timestamp, logging level, and message.
### 2. Modify the function to use different formats for the file and console handlers.
import logging

logger = logging.getLogger("MyApp")
logger.setLevel(logging.DEBUG)

console_log=logging.StreamHandler()
console_log.setLevel(logging.DEBUG)
console_format=logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
console_log.setFormatter(console_format)

file_log=logging.FileHandler('logs/q3 app.log')
file_log.setLevel(logging.DEBUG)
file_format=logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s -> Done by the great file logger',
    datefmt='%Y-%m-%d %H:%M:%S',
)
file_log.setFormatter(file_format)

logger.addHandler(console_log)
logger.addHandler(file_log)

logger.debug("This is a message from Logger")
logger.info("This is a INFO message from Logger")
logger.error("This is an ERROR message from Logger")
logger.critical("This is a CRITICAL message from Logger")