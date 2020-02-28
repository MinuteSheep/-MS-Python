import logging

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='test.log', format = LOG_FORMAT)

logging.debug('My level is debug')
logging.warning('My level is warning')
logging.error('My level is error')
