### Assignment 8: Logging in a Multi-Module Application

### 1. Write a Python script that sets up logging for a multi-module application. 
#      Each module should have its own logger.
### 2. Modify the script to propagate log messages from each module's logger
#      to a root logger that handles logging to a file.

import logging
from module1 import Arithmetic
from module2 import Scientific

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/q8 app.log",
    filemode="a"
)

root_logger = logging.getLogger()
root_logger.info("Application started")

a = Arithmetic.add(10, 5)
b = Scientific.SQRT(49)
c = Arithmetic.divison(10, 0)

root_logger.info(f"Results: add={a}, sqrt={b}, div={c}")