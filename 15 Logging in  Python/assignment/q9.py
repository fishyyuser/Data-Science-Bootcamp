### Assignment 9: Logging Performance

### 1. Write a Python script to benchmark the performance of logging with different handlers
#      (e.g., file handler, console handler, rotating file handler).
### 2. Modify the script to compare the performance of logging with and without message formatting.

import logging
import time
from logging.handlers import RotatingFileHandler

def benchmark_logger(logger, num_messages=10000):
    start = time.time()
    for i in range(num_messages):
        logger.debug("This is a debug log message %d", i)
    end = time.time()
    return end - start


console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("logs/q9perf_file.log", mode="w")
rot_handler = RotatingFileHandler("logs/q9perf_rotating.log", maxBytes=1024*1024, backupCount=3)

handlers = {
    "console": console_handler,
    "file": file_handler,
    "rotating_file": rot_handler,
}

print("\n=== Benchmark WITH formatting ===")
for name, handler in handlers.items():
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.handlers = []  # clear existing
    logger.addHandler(handler)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

    elapsed = benchmark_logger(logger)
    print(f"{name:15}: {elapsed:.3f} seconds")


print("\n=== Benchmark WITHOUT formatting ===")
for name, handler in handlers.items():
    logger = logging.getLogger(name + "_nofmt")
    logger.setLevel(logging.DEBUG)
    logger.handlers = []
    logger.addHandler(handler)
    handler.setFormatter(logging.Formatter("%(message)s"))

    elapsed = benchmark_logger(logger)
    print(f"{name:15}: {elapsed:.3f} seconds")
