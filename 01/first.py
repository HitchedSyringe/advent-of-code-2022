
# Part 1 of Day 1 of Advent of Code 2022.

from pathlib import Path


with open(Path(__file__).parent / "inputs.txt") as f:
    content = f.read()

    print(content.split("\n\n"))

    elves = [[int(i) for i in c.split("\n") if i] for c in content.split("\n\n")]

    most_calories = sum(max(elves, key=sum))

print("Elf carrying most Calories count: ", most_calories)
