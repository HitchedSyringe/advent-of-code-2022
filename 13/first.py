
# Part 1 of Day 13 of Advent of Code 2022.

from pathlib import Path

from _shared import _compare, _parse_packet_pairs


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

pairs = _parse_packet_pairs(content)
ordered = sum(i for i, (l, r) in enumerate(pairs, 1) if _compare(l, r) == 1)

print("Ordered indices sum: ", ordered)
