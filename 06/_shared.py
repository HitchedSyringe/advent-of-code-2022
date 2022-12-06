import collections
from itertools import islice
from pathlib import Path


# itertools recipe from https://docs.python.org/3/library/itertools.html#itertools.islice
def _sliding_window(iterable, *, size):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, size), maxlen=size)

    if len(window) == size:
        yield tuple(window)

    for x in it:
        window.append(x)
        yield tuple(window)


def find_start_marker(content: str, *, window_size: int) -> int:
    """Finds the start of a given packet.

    This utilizes the sliding window approach for finding the start marker.

    For reference:

        start-of-packet: First 4 distinct chars; window_size = 4
        start-of-message: First 14 distinct chars; window_size = 14

    Parameters
    ----------
    content: :class:`str`
        The datastream buffer.
    window_size: :class:`int`
        The window size for the sliding window iteration algorithm.

    Returns
    -------
    :class:`int`
        Start marker for given data.
    """
    start = 0

    for pos, chars in enumerate(_sliding_window(content, size=window_size)):
        if len(set(chars)) == window_size:
            break

        start = pos + window_size + 1

    return start
