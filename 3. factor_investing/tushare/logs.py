#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 01:15:47 2018

@author: song
"""

from __future__ import print_function
import os
import sys
import logging
from logging.handlers import RotatingFileHandler


class ProjectLogger:
    def __init__(self, loggerPath=None, loggerName=None, loggerMode=None):
        self.loggerPath = loggerPath
        os.makedirs(self.loggerPath, exist_ok=True)
        self.loggerName = loggerName
        self.loggerMode = loggerMode

    def create_logger(self):
        """
        Default filemode is append 'a'
        You can use: 
            1. write: 'w'
            2. append: 'a'
            3. read: 'r'
            4. create: 'x'
        """
        # create logger for "Sample App"
        logger = logging.getLogger(self.loggerName)

        if not logger.handlers:
            logger.setLevel(logging.DEBUG)

            # # create file handler which logs detailed information (everything)
            # fh1 = logging.FileHandler(
            #     os.path.join(self.loggerPath, "DEBUG.log"), mode=self.loggerMode
            # )
            # fh1.setLevel(logging.DEBUG)

            # add a rotating handler
            # limitign the size of log file to 100MB, with 2 backups
            fh1 = RotatingFileHandler(
                os.path.join(self.loggerPath, "DEBUG.log"),
                mode=self.loggerMode,
                maxBytes=100000000,
                backupCount=2
            )
            fh1.setLevel(logging.DEBUG)

            # create file handler which logs info as things work as expected
            # fh2 = logging.FileHandler(
            #     os.path.join(self.loggerPath, "INFO.log"), mode=self.loggerMode
            # )
            # fh2.setLevel(logging.INFO)

            # create file handler which logs warning (things not working with minor effect, may not need to change the code)
            # fh3 = logging.FileHandler(
            #     os.path.join(self.loggerPath, "WARNING.log"), mode=self.loggerMode
            # )
            # fh3.setLevel(logging.WARNING)

            # create file handler which logs error (things not working with major effect, may need to change the code)
            fh4 = logging.FileHandler(
                os.path.join(self.loggerPath, "ERROR.log"), mode=self.loggerMode
            )
            fh4.setLevel(logging.ERROR)

            # create console handler with a higher log level
            # ch = logging.StreamHandler(stream=sys.stdout)
            # ch.setLevel(logging.DEBUG)

            # create formatter and add it to the handlers
            formatter = logging.Formatter(
                "[%(asctime)s] %(levelname)8s --- %(message)s "
                + "(%(filename)s:%(lineno)s)",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            fh1.setFormatter(formatter)
            # fh2.setFormatter(formatter)
            # fh3.setFormatter(formatter)
            fh4.setFormatter(formatter)
            # ch.setFormatter(formatter)

            # add the handlers to the logger
            logger.addHandler(fh1)
            # logger.addHandler(fh2)
            # logger.addHandler(fh3)
            logger.addHandler(fh4)
            # logger.addHandler(ch)

        return logger


class TushareLogger:
    @classmethod
    def get_logger(cls):
        pl = ProjectLogger(
            loggerPath="./log",
            loggerName=cls.__name__,
            loggerMode="w"
        )
        return pl.create_logger()


if __name__ == "__main__":
    ts_logger = TushareLogger.get_logger()
    print(ts_logger)
