### Assignment 2: Logging with Different Handlers
### 1. Write a Python function to create a logger that logs messages to both a file named `app.log` and the console.
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("logs/q2 app.log"),
        logging.StreamHandler()
    ]
)
logging.debug("This is a message from Logger")
logging.info("This is a INFO message from Logger")
logging.error("This is an ERROR message from Logger")
logging.critical("This is a CRITICAL message from Logger")

