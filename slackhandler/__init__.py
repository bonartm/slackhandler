from datetime import datetime as dt
import logging
import requests
import slackhandler.blockkit as kit

class SlackHandler(logging.Handler):

    emojis = {
        'DEBUG': ':face_with_monocle:',
        'INFO': ':slightly_smiling_face:',
        'WARNING': ':thinking_face:',
        'ERROR': ':cry:',
        'EXCEPTION': ':cry:',
        'CRITICAL': ':zany_face:'
    }

    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url=url

    def _make_message(self, record, emoji):
        time = (dt.utcfromtimestamp(record.created).
                strftime('%Y-%m-%d %H:%M:%S'))
        blocks = kit.make_blocks(
            kit.make_context(
                kit.make_markdown(emoji),
                kit.make_markdown(f'*Level*: {record.levelname}'),
                kit.make_markdown(f'*Logger*: {record.name}'),
                kit.make_markdown(f'*File*: {record.filename}')),
            kit.make_section(f'*{record.levelname} message from {record.name}: *'),
            kit.make_section(record.msg),
            kit.make_divider())

        return {"blocks": blocks}


    def emit(self, record):
        emoji = self.emojis[record.levelname]
        resp = requests.post(
            url=self.url, 
            json = self._make_message(record, emoji))
        return resp.content