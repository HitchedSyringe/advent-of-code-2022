
# Part 1 of Day 3 of Advent of Code 2022.

import string
from pathlib import Path

path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

rucksacks = content.splitlines()

priorities = {c: i for i, c in enumerate(string.ascii_letters, 1)}

priority_sum = 0

for rucksack in rucksacks:
    half = len(rucksack) // 2

    first = rucksack[:half]
    second = rucksack[half:]

    intersecting = set(first).intersection(second)

    for item in intersecting:
        priority_sum += priorities[item]


print("The priority sum is: ", priority_sum)
