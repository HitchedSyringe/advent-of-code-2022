
# Part 1 of Day 9 of Advent of Code 2022.

from pathlib import Path

from _shared import get_unique_tail_position_count


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

lines = content.splitlines()

print("Unique tail positions: ", get_unique_tail_position_count(lines, 2))
