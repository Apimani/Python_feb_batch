import logger
# 1. CRITICAL==>50==>Represents a very serious problem that needs high attention
# 2. ERROR===>40===>Represents a serious error
# 3. WARNING==>30==>Represents a warning message, some caution needed. It is alert to
# the programmer
# 4. INFO===>20===>Represents a message with some important information
# 5. DEBUG===>10==>Represents a message with debugging information
# 6. NOTSET==>0==>Rrepresents that the level is not set.


# %(asctime)s: The timestamp of the log message in the format specified by the datefmt parameter (if provided).
# %(levelname)s: The log level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
# %(message)s: The log message itself.
# %(name)s: The name of the logger.
# %(filename)s: The name of the file containing the logger call.
# %(lineno)d: The line number where the logger call occurred.
# %(funcName)s: The name of the function/method where the logger call occurred.


logger.basicConfig(filename='new.txt', filemode='a', level=logger.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s - %(name)s-%(funcName)s-%(lineno)d')
logger = logger.getLogger()

#NDIWEC

logger.debug("debug")

logger.info("info")
logger.warning("warn")
logger.error("error")
logger.critical("critical")