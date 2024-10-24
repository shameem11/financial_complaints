from constants import TIMESTAMP
import os 
import logging

LOG_DIR = "logs"
LOG_FILE_NAME = f"log_{TIMESTAMP}.log"
os.makedirs(LOG_DIR,exit=True)
LOG_DIR_PATH = os.path(LOG_DIR,LOG_FILE_NAME)


logging.basicConfig(filename=LOG_FILE_NAME,
                    filemode="w",
                    format="[%(asctime)s] \t%(levelname)s \t%(lineno)d \t%(filename)s  \t%(funcName)s() \t%(message)s",
                    level=logging.INFO) 