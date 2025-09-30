import multiprocessing
import math
### import sys
import time

### sys.set_int_max_str_digits(100000) ### commented bcoz my virtual environment uses python 3.10
                                       ### and this method was introduced after python 3.11+ to prevent Deniel of service

def factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[10000,20000,30000,40000,50000]
    
    start_time=time.time()

    with multiprocessing.Pool() as pool:
        results=pool.map(factorial,numbers)
    
    end_time=time.time()

    print(f"Results : {results}")
    print(f"Execution time :{end_time-start_time}")
