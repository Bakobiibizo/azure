import responses
from src.system_tools.logger import LoggerInstance, LoggerConfig

@responses.activate
def test_http_logger():
    url = 'http://test.com'
    responses.add(responses.POST, url)  
    logger = LoggerInstance(log_file='tests/json_test_files/test_log.log', logging_mode='http', url=url)
    logger.log('test')
    assert len(responses.calls) == 1

def test_local_logger():
    log_file = "tests/json_test_files/test_log.log"
    config = LoggerConfig(log_file=log_file, logging_mode='local', mode='a')
    logger = LoggerInstance(log_file=config.log_file, logging_mode=config.logging_mode) 
    logger.log('test')
    with open(log_file, 'r') as f:
        assert 'test' in f.read()