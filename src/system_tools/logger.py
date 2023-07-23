import sys
from pydantic import BaseModel, validator
from typing import Optional
import logging
import requests


class LoggerConfig(BaseModel):
    logging_mode: Optional[str]
    log_file: Optional[str] 
    url: Optional[str]
    mode: Optional[str]

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

class Logger(BaseModel):
    def __init__(self, config: LoggerConfig):
        self.log_file = config.log_file
        self.logging_mode = config.logging_mode
        self.url = config.url
        self.mode = config.mode
        self.level = config.level
        if not self.log_file:
            self.log_file = "src/static/log/app.log"
        if not self.logging_mode:
            self.logging_mode = "local"
        if not self.url:
            self.url = "https://test.com"
        if not self.mode:
            self.mode = "a"
        self.config = LoggerConfig(log_file=self.log_file, logging_mode=self.logging_mode, url=self.url, mode=self.mode)
        self.logger = self.logging.getLogger(__name__)
        self.select_logger(logging_mode=self.logging_mode, level=self.level)

    def select_logger(self, logging_mode, level):
        if logging_mode=="http":
            HttpLogger(self, logging_mode, level)
        elif logging_mode=="local":
            LocalLogger(self, logging_mode, level)


    def set_level(self, msg=None, level=None):
        if not msg:
            raise ValueError("msg required")
        if not level:
            level = "info"
        if level == "info":
            self.logger.info(msg)
        elif level == "warning":
            self.logger.warning(msg)
        elif level == "error":
            self.logger.error(msg)
        elif level == "critical":
            self.logger.critical(msg)
        elif level == "fatal":
            self.logger.fatal(msg)

    def log(self, msg, level):
        self.set_level(msg=msg, level=level)


class LocalLogger(Logger):
    def __init__(self):
        self.handler = logging.FileHandler(filename=self.config.log_file, mode=self.config.mode)
        self.handler.setLevel(logging.INFO)  
        self.logger.addHandler(self.handler)
        self.set_level(msg="Initialized Local Logger")
        


class HttpLogger(Logger):
    def __init__(self):
        self.stream_handler = logging.StreamHandler(filename=self.config.log_file, mode=self.config.mode)
        self.handler.setLevel(logging.INFO)  
        self.logger.addHandler(self.handler)
        self.set_level(msg = "Initialized HTTP Logger")




