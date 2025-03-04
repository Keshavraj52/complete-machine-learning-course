
import multiprocessing
import math
import multiprocessing.pool
import sys
import time

sys.set_int_max_str_digits(1000000000)
## function to compute factorial of given number 

def computer_factorial(number):
    print(f"compute factorial of {number}")
    result=math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result
if __name__=="__main__":
    numbers=[5000,6440,4342,2344]
    start_time=time.time()
    ## create  a pool of worker processess
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)

    end_time=time.time()

    print(f"results: {results}")
    print(f"time taken: {end_time - start_time} sec")