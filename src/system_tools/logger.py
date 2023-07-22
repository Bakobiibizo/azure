from pydantic import BaseModel, validator
from typing import Optional
import logging
import requests

class LoggerConfig(BaseModel):
    mode: Optional[str] = "local" 
    log_file: Optional[str] = "src/static/log/app.log"
    url: Optional[str] = None

    @validator('mode')
    def validate_mode(cls, value):
        if value not in ['local', 'http']:
            raise ValueError('mode must be local or http')
        return value

    @validator('url')
    def validate_url(cls, value, values):
        if values['mode'] == 'http' and not value:
            raise ValueError('url required for http mode')
        return value

class LocalLogger:
    def __init__(self, config):
        self.config = config
        logging.basicConfig(filename=self.config.log_file) 

    def log(self, msg, level='info'):
        if level == 'info':
            logging.info(msg)
        elif level == 'warning':
            logging.warning(msg)
        elif level == 'error':
            logging.error(msg)
        else:
            logging.debug(msg)

class HttpLogger:
    def __init__(self, config):
        self.config = config

    def log(self, msg, level='info'):
        data = {'message': msg, 'level': level}
        requests.post(self.config.url, data=data)

class Logger:
    def __init__(self, config):
        self.config = config
        if self.config.mode == 'local':
            self.logger = LocalLogger(config)
        elif self.config.mode == 'http':
            self.logger = HttpLogger(config)
        else:
            raise ValueError('Invalid mode')
        self.get()    
    def get(self):
        return self.logger

    def log(self, msg, level='info'):
        self.logger.log(msg, level)

class LoggerInstance:
    def __init__(self, log_file, mode, url=None, level='info'):
        config = LoggerConfig(log_file=log_file, mode=mode, url=url)
        self.logger = Logger(config)

    def get_logger(self):
        return self.logger

    def log(self, msg, level='info'):
        self.logger.log(msg, level)