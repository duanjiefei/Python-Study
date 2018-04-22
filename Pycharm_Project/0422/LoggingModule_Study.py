import logging
#
# logging.basicConfig(
#     level = logging.DEBUG,
#     filename = "log.txt",
#     filemode="w",
#    # datefmt="",
#     format="%(asctime)s %(filename)s [%(lineno)d] %(message)s"
# )
#
#
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

logger = logging.getLogger()

fh = logging.FileHandler("test_logger.txt")
ch = logging.StreamHandler()

fm = logging.Formatter("%(asctime)s %(message)s")

fh.setFormatter(fm)
ch.setFormatter(fm)

logger.addHandler(fh)
logger.addHandler(ch)

logger.setLevel("DEBUG")


logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")