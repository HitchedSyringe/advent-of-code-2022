
# Part 1 of Day 4 of Advent of Code 2022.

from pathlib import Path


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

pairs = content.splitlines()

full_overlaps = 0

def as_range(assignment):
    first, last = assignment.split("-")
    return range(int(first), int(last) + 1)

for pair in pairs:
    first, second = pair.split(",")

    first = set(as_range(first))
    second = set(as_range(second))

    if first.issubset(second) or second.issubset(first):
        full_overlaps += 1


print("Full overlaps: ", full_overlaps)
