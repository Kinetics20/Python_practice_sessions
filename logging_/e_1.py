import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)-8s - %(name)-10s: %(message)s')

log = logging.getLogger(__name__)

log.debug('debug message')
log.info('info message')
log.warning('warning message')
log.error('error message')
log.critical('critical message')
