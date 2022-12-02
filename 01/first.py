
# Part 1 of Day 1 of Advent of Code 2022.

from pathlib import Path


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

elves = [[int(i) for i in c.split("\n") if i] for c in content.split("\n\n")]

most_calories = sum(max(elves, key=sum))

print("Elf carrying most Calories count: ", most_calories)
