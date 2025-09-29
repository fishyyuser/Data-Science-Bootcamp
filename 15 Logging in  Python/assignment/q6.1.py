### Assignment 6: Contextual Logging

### 1. Write a Python function to create a logger that includes contextual information
###    (e.g., function name, line number) in the log messages.
### 2. Modify the function to include additional contextual information (e.g., user ID, session ID).
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(function_name)s- %(line_no)s- %(message)s",
    filename="logs/q6 app.log",
    filemode="a"
)

def add(a,b):
    result=a+b
    logging.debug("This function is adding",extra={'function_name': 'add', 'line_no': 18})
    return result

add(5,6)