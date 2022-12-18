"""
Shared components for Day 6 solutions.
Copyright (C) 2022-present HitchedSyringe

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import collections
from itertools import islice


# itertools recipe from https://docs.python.org/3/library/itertools.html#itertools.islice
# Copyright (C) 2001-present Python Software Foundation
# Dual-licensed under the PSF License Version 2 and the Zero-Clause BSD license.
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
