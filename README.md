# slackhandler

A simple handler for python's `logging` module. It posts logging messages in a slack channel.

## installation

```
pip install git+git://github.com/bonartm/slackhandler.git
```

## usage

Setup a slack app with [webhooks](https://api.slack.com/messaging/webhooks) and pass the provided endpoint url into the handler:

```python
import logging
from slackhandler import SlackHandler

WEBHOOK = 'https://hooks.slack.com/services/example'
handler = SlackHandler(url=WEBHOOK)
logger = logging.getLogger('test_logger')
logger.addHandler(handler)
logger.critical('help! help!')
```
