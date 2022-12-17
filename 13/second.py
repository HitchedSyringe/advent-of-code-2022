
# Part 2 of Day 13 of Advent of Code 2022.

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
