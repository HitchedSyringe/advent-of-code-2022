
# Part 2 of Day 3 of Advent of Code 2022.

import string
from pathlib import Path


def chunk(iterable, *, size=1):
    length = len(iterable)

    for index in range(0, length, size):
        yield iterable[index:min(index + size, length)]

path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

rucksacks = content.splitlines()

priorities = {c: i for i, c in enumerate(string.ascii_letters, 1)}

priority_sum = 0

for first, second, third in chunk(rucksacks, size=3):
    intersecting = set(first).intersection(second, third)

    for item in intersecting:
        priority_sum += priorities[item]


print("The priority sum is: ", priority_sum)
