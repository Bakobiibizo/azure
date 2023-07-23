import responses
from src.system_tools.logger import Logger, LoggerConfig

config = LoggerConfig(log_file="tests/json_test_files/test_log.log", logging_mode="local", url=None, mode="a")
logger = Logger(config)
logger.log("Initialized test_messages.py:")

@responses.activate
def test_http_logger():
    url = 'http://test.com'

    assert len(responses.calls) == 1

import time

def test_local_logger():
    logger.log('test')
    time.sleep(1)  # wait for the log message to be written
    with open(logger.config.log_file, 'r') as f:
        assert 'test' in f.read()