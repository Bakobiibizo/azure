import responses
from src.system_tools.logger import get_logger

@responses.activate
def test_http_logger():
    url = 'http://test.com'
    responses.add(responses.POST, url)  
    logger = get_logger(log_file='tests/json_test_files/test_log.log', mode='http', url=url)
    logger.log('test')
    assert len(responses.calls) == 1

def test_local_logger():
    log_file = "tests/json_test_files/test_log.log"
    logger = get_logger(log_file=log_file, mode='local') 
    logger.log('test')
    assert 'test' in log_file.read_text()