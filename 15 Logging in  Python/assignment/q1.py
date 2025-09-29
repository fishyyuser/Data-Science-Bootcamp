### Assignment 1: Basic Logging
### 1. Write a Python function to create a basic logger that logs messages to a file named `app.log`.
import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename='logs/app.log',
    filemode='a',
    format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.debug("This is message from debugger")

### 2. Modify the function to log messages of levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL.
logging.debug("This is another message from debugger")
logging.info("This is a INFO message from Logger")
logging.error("This is an ERROR message from Logger")
logging.critical("This is a CRITICAL message from Logger")