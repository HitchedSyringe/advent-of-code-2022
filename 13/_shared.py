"""
Shared components for Day 13 solutions.
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


from __future__ import annotations

import itertools
import json
from typing import TYPE_CHECKING, List, Optional, Tuple, Union


if TYPE_CHECKING:
    Packet = Union[list, int]


def _parse_packet_pairs(content: str) -> List[Tuple[Packet, Packet]]:
    """Parses the given input to readable packet pairs."""
    packet_pairs = []

    for couplet in content.split("\n\n"):
        # Padding is needed for the trailing space at the end.
        left, right, *_ = couplet.split("\n")

        left = json.loads(left)
        right = json.loads(right)

        packet_pairs.append((left, right))

    return packet_pairs


def _compare(left: Optional[Packet], right: Optional[Packet]) -> int:
    """Compares the left and right packets and returns an
    :class:`int` indicating the status of the packet pair.

    The possible statuses are as follows:
        * 1: Packet pair is in the right order.
        * 0: Status indeterminant; For internal use only.
        * -1: Packet pair is not in the right order.

    Ultimately, the final status should either be 1 or -1.
    """
    if left is None:
        return 1

    if right is None:
        return -1

    left_is_list = isinstance(left, list)
    right_is_list = isinstance(right, list)

    if left_is_list and right_is_list:
        for l, r in itertools.zip_longest(left, right):
            status = _compare(l, r)

            if status != 0:
                return status
    elif left_is_list:
        return _compare(left, [right])
    elif right_is_list:
        return _compare([left], right)
    elif left > right:
        return -1
    elif left < right:
        return 1

    return 0
