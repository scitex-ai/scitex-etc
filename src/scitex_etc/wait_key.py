#!/usr/bin/env python3
# File: src/scitex_etc/wait_key.py

import multiprocessing
import time

import readchar
import scitex_logging as slogging

_console = slogging.getPlainConsole(__name__)


def _emit(value):
    """Write ``value`` as one unprefixed line to stdout via scitex-logging."""
    _console.emit(str(value))


def wait_key(p, *, read_key=None, printer=_emit):
    """Block until the user presses ``q``, then terminate process ``p``.

    Echoes each key as it is pressed; on ``q`` prints a notice and calls
    ``p.terminate()``.

    Parameters
    ----------
    p
        A process-like object exposing ``terminate()``.
    read_key : callable, optional
        Zero-arg callable returning the next key as a string. Defaults to
        ``readchar.readchar``. Injectable as a test seam (no mocks).
    printer : callable, optional
        Output sink, defaults to an unprefixed scitex-logging stdout line.
        Injectable so tests can record output without patching stdout.
    """
    if read_key is None:
        read_key = readchar.readchar
    key = "x"
    while key != "q":
        key = read_key()
        printer(key)
    printer("q was pressed.")
    p.terminate()


def count(*, printer=_emit, sleeper=time.sleep):
    """Print an incrementing counter forever, sleeping 1s between values.

    Parameters
    ----------
    printer : callable, optional
        Output sink, defaults to an unprefixed scitex-logging stdout line.
        Injectable test seam.
    sleeper : callable, optional
        One-arg sleep callable, defaults to ``time.sleep``. Injectable so
        tests can run without real delay and bound the loop.
    """
    counter = 0
    while True:
        printer(counter)
        sleeper(1)
        counter += 1


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=count)

    p1.start()
    wait_key(p1)
    _emit("aaa")

# EOF
