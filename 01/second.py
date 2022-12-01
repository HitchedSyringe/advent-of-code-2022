
# Part 2 of Day 1 of Advent of Code 2021.

from pathlib import Path


with open(Path(__file__).parent / "inputs.txt") as f:
    content = f.read()

    print(content.split("\n\n"))

    elves = [[int(i) for i in c.split("\n") if i] for c in content.split("\n\n")]
    elves.sort(key=sum, reverse=True)

    elves_most_calories = elves[:3]

    most_calories = sum(sum(elf) for elf in elves_most_calories)

print("Top 3 Elves carrying most Calories count: ", most_calories)
