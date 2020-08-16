
"""
This file is responsible for running all of the functions identified by app.py
"""

from util.argparse_constants import *

def command(argument,
            test=False):
    """uses a dictionary as a switch statement to determine which function to run"""
    import entrypoints.entry_character as entry_character

    switcher = {
        showchar_cmd: entry_character.show_char,
    }

    if hasattr(argument, "which"):
        func = switcher.get(argument.which)
        try:
            output = func(argument)
        except Exception as e:
            raise e
        return output
    else:
        return None