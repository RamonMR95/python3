import logging

logging.basicConfig(filename="err_log.log", level=logging.ERROR)
logging.critical("critical")
logging.error("Error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")
