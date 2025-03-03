from concurrent.futures import ProcessPoolExecutor

import time

def print_number(number):
    time.sleep(3)
    return f"number :{number*number}"
numbers=[1,2,3,4,5,6,6,7,8]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        results=executor.map(print_number,numbers)

    for result in results:
        print(result)