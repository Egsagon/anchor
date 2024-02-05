import os
import re
from typing import Literal

class COLOR:
    NORMAL = 0
    RED = 91
    GREEN = 92
    GREY = 90

class BORDER:
    CLASSIC = '-|++++'


# --- Default configuration --- #
MAX_WIDTH    = 100              #
FONT_COLOR   = COLOR.NORMAL     #
BORDER_TYPE  = BORDER.CLASSIC   #
BORDER_COLOR = COLOR.GREY       #
#  ---------------------------- #

_justify = Literal['left', 'right', 'center']

_justifier = {
    'left'  : str.ljust,
    'right' : str.rjust,
    'center': str.center
}

_re_ansi   = re.compile(r'\x1b\[(.+?)m'       )
_re_italic = re.compile(r'(\*)(.+?)(\*)'      )
_re_bold   = re.compile(r'(\*\*)(.+?)(\*\*)'  )
_re_color  = re.compile(r'\$([A-Z]+)\((.+?)\)')

def ansi(code: int | str = 0) -> str:
    return f'\x1b[{code}m'

def width() -> int:
    '''
    Get the max allowed terminal width.
    '''
    
    return min(MAX_WIDTH, os.get_terminal_size().columns)


def _header(title: str = None, justify: _justify = 'left') -> None:
    '''
    Print a header.
    '''
    
    title = f' {title.strip()} ' if title else ''
    line = _justifier[justify](title, width() - 2, BORDER_TYPE[0])
    
    print(ansi(BORDER_COLOR)
          + BORDER_TYPE[2]
          + line
          + BORDER_TYPE[3]
          + ansi())

def _footer() -> None:
    '''
    Print a footer.
    '''
    
    print(ansi(BORDER_COLOR)
          + BORDER_TYPE[2]
          + BORDER_TYPE[0] * (width() - 2)
          + BORDER_TYPE[3]
          + ansi())

def banner(text: str | list[str],
           justify: _justify = 'center',
           title: str = None,
           justify_title: _justify = 'left') -> None:
    '''
    Write a banner.
    '''
    
    lines = text
    if isinstance(text, str):
        lines = text.split('\n')
        
    _header(title, justify_title)
    
    for line in lines:
        
        # Format
        formated = _re_bold.sub(ansi(1) + '\g<2>' + ansi(22), line)
        formated = _re_italic.sub(ansi(3) + '\g<2>' + ansi(23), formated)
        formated = _re_color.sub('\x1b[{\g<1>}m\g<2>\x1b[0m', formated).format(**COLOR.__dict__)
        
        ansi_length = sum(map(lambda m: len(m) + 3, _re_ansi.findall(formated)))
        
        body = _justifier[justify](formated, width() - 2 + ansi_length)
        
        print(ansi(BORDER_COLOR)
              + BORDER_TYPE[1]
              + ansi(FONT_COLOR)
              + body
              + ansi(BORDER_COLOR)
              + BORDER_TYPE[1]
              + ansi(0))
    
    _footer()

# TODO
# SELECT
# ENTRY
# SEPARATOR
# TQDM BAR

# wrap text too big for one banner line :)


# EOF