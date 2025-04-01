class Format:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

print(Format.BOLD + Format.UNDERLINE + 'Hello')