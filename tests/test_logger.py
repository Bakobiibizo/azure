import responses
from src.system_tools.logger import LoggerInstance

@responses.activate
def test_http_logger():
    url = 'http://test.com'
    responses.add(responses.POST, url)  
    logger = LoggerInstance(log_file='tests/json_test_files/test_log.log', mode='http', url=url)
    logger.log('test')
    assert len(responses.calls) == 1

def test_local_logger():
    log_file = "tests/json_test_files/test_log.log"
    logger = LoggerInstance(log_file=log_file, mode='local') 
    logger.log('test')
    with open(log_file, 'r') as f:
        assert 'test' in f.read()