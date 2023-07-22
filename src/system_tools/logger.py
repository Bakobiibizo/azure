import sys
from pydantic import BaseModel, validator
from typing import Optional
import logging
import requests

class Logger:
    def __init__(self, log_file=None, logging_mode="local", url=None, mode="a"):
        self.config = LoggerConfig(log_file=log_file, logging_mode=logging_mode, url=url, mode=mode)
        self.logger = logging.getLogger(__name__)
        self.mode = self.config.mode
        handler = logging.FileHandler(filename=self.config.log_file, mode=self.mode)
        handler.setLevel(logging.INFO)  
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO) 
        stream_handler = logging.StreamHandler(sys.stdout)  
        self.logger.addHandler(stream_handler)  

    def get(self):
        return self.logger

    def log(self, msg=None, level="info"):
        if not msg:
            pass
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


class LocalLogger(Logger):
    def __init__(self, log_file=None, logging_mode="local", url=None, mode=None):
        return self.get

    def get_logger(self):
        return self.logger

class HttpLogger(Logger):
    def __init__(self, config):
        self.config = config

    def log(self, msg=None, level="info"):
        if not msg:
            msg = "Init Value or no log entry"
        data = {"message": msg, "level": level}
        requests.post(self.config.url, data=data)



