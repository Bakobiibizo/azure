from pydantic import BaseModel, validator
from typing import Optional
import logging
import requests

class Logger:
    def __init__(self, config):
        self.config = config
        if self.config.logging_mode == "local":
            self.logger = LocalLogger(config)
        elif self.config.logging_mode == "http":
            self.logger = HttpLogger(config)
        else:
            raise ValueError("Invalid logging_mode")
        self.get()    
    def get(self):
        return self.logger

    def log(self, msg=None, level="info"):
        if not msg:
            msg = "Init Value or no log entry"
        self.logger.log(msg, level)

class LoggerConfig(BaseModel):
    logging_mode: Optional[str] = "local" 
    log_file: Optional[str] = "src/static/log/app.log"
    url: Optional[str] = None
    mode: Optional[str] = "a"

    @validator("logging_mode")
    def validate_mode(cls, value):
        if value not in ["local", "http"]:
            raise ValueError("logging_mode must be local or http")
        return value

    @validator("url")
    def validate_url(cls, value, values):
        if values["logging_mode"] == "http" and not value:
            raise ValueError("url required for http logging_mode")
        return value

import sys

class LocalLogger(Logger):
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.mode = self.config.mode
        handler = logging.FileHandler(filename=self.config.log_file, mode=self.mode)
        handler.setLevel(logging.INFO)  # set handler level
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)  # set logger level
        stream_handler = logging.StreamHandler(sys.stdout)  # create stream handler
        self.logger.addHandler(stream_handler)  # add stream handler to the logger


    def log(self, msg=None, level="info"):
        if not msg:
            msg = "Init Value or no log entry"
        print(f"Logging message: {msg} at level: {level}")  # Debug print statement
        if level == "info":
            self.logger.info(msg)
        elif level == "warning":
            self.logger.warning(msg)
        elif level == "error":
            self.logger.error(msg)
        else:
            self.logger.debug(msg)
        for handler in self.logger.handlers:
            handler.flush()

class HttpLogger(Logger):
    def __init__(self, config):
        self.config = config

    def log(self, msg=None, level="info"):
        if not msg:
            msg = "Init Value or no log entry"
        data = {"message": msg, "level": level}
        requests.post(self.config.url, data=data)

class LoggerInstance(Logger):
    def __init__(self, log_file="src/static/log/app.log", logging_mode="local", url=None, level="info", mode="a"):
        config = LoggerConfig(log_file=log_file, logging_mode=logging_mode, url=url, mode="a")
        self.logger = Logger(config)

    def get_logger(self):
        log_file = "tests/json_test_files/test_log.log"
        config = LoggerConfig(log_file=log_file, logging_mode="local", mode="a")
        logger = LoggerInstance(log_file=config.log_file, logging_mode=config.logging_mode) 
        logger.log(level="info")
        self.logger = logger
        return self.logger

    def log(self, msg=None, level="info"):
        self.logger.log(msg, level)

