### 2. Modify the function to use different logging levels for the file and console handlers.
import logging

logger = logging.getLogger("MyApp")
logger.setLevel(logging.DEBUG)

console_log=logging.StreamHandler()
console_log.setLevel(logging.ERROR)
console_format=logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
console_log.setFormatter(console_format)

file_log=logging.FileHandler('logs/q2 app.log')
file_log.setLevel(logging.DEBUG)
file_format=logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
file_log.setFormatter(file_format)

logger.addHandler(console_log)
logger.addHandler(file_log)

logger.debug("This is a message from Logger")
logger.info("This is a INFO message from Logger")
logger.error("This is an ERROR message from Logger")
logger.critical("This is a CRITICAL message from Logger")