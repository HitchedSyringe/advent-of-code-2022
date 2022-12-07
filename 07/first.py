
# Part 1 of Day 7 of Advent of Code 2022.

from pathlib import Path

from _shared import get_directory_sizes


TARGET_SIZE = 100000

path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

counts = get_directory_sizes(content)

total = sum(v for v in counts.values() if v <= TARGET_SIZE)

print("Sum of directories with size <= 100000: ", total)
