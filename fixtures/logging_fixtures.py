import pytest
import logging
from config.test_conf import Config


@pytest.fixture(scope="function", autouse=True)
def logger(request):
    log_file = logging.FileHandler('test_case.log', 'a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_file.setFormatter(formatter)
    Config.logger = logging.getLogger(request.function.__name__)
    Config.logger.setLevel(logging.DEBUG)
#    for hdlr in Config.logger.handlers[:]:  # remove all old handlers
#        logger.removeHandler(hdlr)
    Config.logger.addHandler(log_file)
