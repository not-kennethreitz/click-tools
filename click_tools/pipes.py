# -*- coding: utf-8 -*-

import sys
import os


def piped_in():
    """Returns piped input via stdin, else None."""
    with sys.stdin as stdin:
        # TTY is only way to detect if stdin contains data
        if not stdin.isatty():
            return stdin.read()
        else:
            return None


def is_interactive():
    """Returns if the current session is interactive or not."""
    return bool(os.isatty(sys.stdout.fileno()))
