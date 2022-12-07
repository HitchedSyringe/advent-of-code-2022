
# Part 2 of Day 7 of Advent of Code 2022.

from pathlib import Path

from _shared import get_directory_sizes


TOTAL_SIZE = 70000000
REQUIRED_FREED = 30000000

path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

counts = get_directory_sizes(content)
free = TOTAL_SIZE - counts["/"]

deleted_size = min(v for v in counts.values() if free + v >= REQUIRED_FREED)

print("Deleted Directory Size: ", deleted_size)
