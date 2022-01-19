

def underline(s):
    return '\n'.join(s, '='*len(s))

def bold(s : str):
    """ bolds string using ANSI escape sequence """
    return f'\33[1m{s}\33[0m'
