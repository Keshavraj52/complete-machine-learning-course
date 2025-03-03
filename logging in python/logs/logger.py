## configuring logging
import logging
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H-%M-%S'
)

logging.debug("this is debu message")
logging.info("this i information message")
logging.warning("this is warning message")
logging.error("this is an error message")
logging.critical("this is a critical message")