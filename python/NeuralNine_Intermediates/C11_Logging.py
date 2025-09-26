import logging

logging.basicConfig(level=logging.DEBUG)
logging.log(logging.CRITICAL,"CRITICAL MESSAGE")
logging.debug("DEBUG MESSAGE")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(levelname)s] - %(asctime)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logging.debug("DEBUG MESSAGE")
logging.debug("DEBUG MESSAGE")
logging.info("INFOMATION")
