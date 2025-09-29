### Assignment 5: Logging Exceptions

### 1. Write a Python function that logs an exception stack trace to a log file when an exception occurs.
### 2. Modify the function to log the stack trace at the ERROR level.
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="logs/q5 app.log",
    filemode="a"
)

try:
    result = 5 / 0
except Exception:
    logging.error("Something went wrong!",exc_info=True)