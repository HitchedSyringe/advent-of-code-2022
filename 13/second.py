"""
Solution to Part 2 of Day 13 of Advent of Code 2022.
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


import functools
import operator
from pathlib import Path

from _shared import _compare, _parse_packet_pairs


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

pairs = _parse_packet_pairs(content)

packets = []

for left, right in pairs:
    packets.extend((left, right))

dividers = ([[2]], [[6]])
packets.extend(dividers)

sorted_ = sorted(packets, key=functools.cmp_to_key(_compare), reverse=True)

key = operator.mul(*(i for i, p in enumerate(sorted_, 1) if p in dividers))

print("Decoder key: ", key)
