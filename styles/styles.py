from prompt_toolkit.styles import Style
from prompt_toolkit import HTML

style = Style.from_dict(
    {
        '': '#edea66',
        'username': '#884444',
        'at': '#00aa00',
        'host': '#00aa00',
        'dollar': '#00bb00',
        'bottom-toolbar': '#ffffff bg:#333333',
        'dialog': 'bg:#88ff88',
        'dialog frame.label': 'bg:#ffffff #000000',
        'dialog.body': 'bg:#000000 #00ff00',
        'dialog shadow': 'bg:#00aa00',
        'dialog.body label': '#fd8bb6',
        'button': 'bg:#bf99a4',
        'checkbox': '#e8612c',
        'frame.label': '#fcaca3',
    }
)

def html_label(text):
    return HTML('<style color="#66b1ed">' + text + '</style>')
