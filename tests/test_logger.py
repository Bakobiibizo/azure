import responses
from src.system_tools.logger import LoggerInstance

instance = LoggerInstance()
logger = instance.get_logger()
logger.log("Initialized Test_Message: \n")

@responses.activate
def test_http_logger():
    url = 'http://test.com'

    assert len(responses.calls) == 1

import time

def test_local_logger():
    logger.log('test')
    time.sleep(1)  # wait for the log message to be written
    with open(log_file, 'r') as f:
        assert 'test' in f.read()