import sys
import logging
import os
from logging import Logger

logging.basicConfig(
    level=logging.getLevelName(os.getenv("LOGGING_LEVEL", "DEBUG")),
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S UTC',
    stream=sys.stdout)


def PlayAppLogger() -> Logger:
    return logging.getLogger('playapp')