def make_divider():
    return {"type": "divider"}

def make_markdown(text):
    return {"type": "mrkdwn", "text": text }

def make_section(text):
    return {"type":"section", "text": make_markdown(text)}

def make_context(*args):
    return {"type":"context", "elements": [*args]}

def make_blocks(*args):
    return [*args]


