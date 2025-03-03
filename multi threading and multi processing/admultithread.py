from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"number :{number}"

numbers=[1,2,3,4,5,6,7,85,5,5,5,9]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_number,numbers)

for result in results:
    print(result)

t=time.time()
print(t)