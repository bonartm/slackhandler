from slackhandler import SlackHandler
import logging
import os

WEBHOOK = os.getenv('SLACK_WEBHOOK')

handler = SlackHandler(url=WEBHOOK)
logger = logging.getLogger('test_logger')
logger.addHandler(handler)

logger.debug('sending some details')
logger.info('everything allright')
logger.warning('mhh, there is something not ok')
logger.error('oh no! something is wrong.')
logger.critical('help! help!')