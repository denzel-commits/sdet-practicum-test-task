import os
import logging
from configuration import LOGS_PATH


class Logger:
    def __init__(self, name, log_level):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)

        if not os.path.isdir(LOGS_PATH):
            os.makedirs(LOGS_PATH)

        formatter = logging.Formatter(
            "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

        file_handler = logging.FileHandler(filename=os.path.join(LOGS_PATH, f"{name}.log"))
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(stream_handler)

    def get_logger(self):
        return self._logger

