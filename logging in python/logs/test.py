from logger import logging
def add(a,b):
    logging.debug("the addition operation taking place")
    return a+b

logging.debug("the addition function calling")

add(10,25)
