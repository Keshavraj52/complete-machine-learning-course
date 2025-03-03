import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H-%M-%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithematicApp")
def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} + {b}={result} ")
    return result
def subtract(a,b):
    result=a-b
    logger.debug(f"subtraction {a} - {b}={result}")
    return result
def multiply(a,b):
    result=a*b
    logger.debug(f"multiply {a} * {b}={result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"division {a} / {b}= {result}")
        return result
    except ZeroDivisionError:
        logger.error("division by zero error")
        return None
    

add(10,15)
subtract(10,15)
multiply(15,25)
divide(80,40)