
# Part 2 of Day 2 of Advent of Code 2022.

from pathlib import Path


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

# Player:
#   X = Lose => 0 points
#   Y = Draw => 3 points
#   Z = Win => 6 points
pairs = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

# Plays:
#   A = Rock
#   B = Paper
#   C = Scissors

# <Opponent Play>: (<Losing Play>, <Drawing Play>, <Winning Play>)
outcome_map = {
    "A": ("C", "A", "B"),
    "B": ("A", "B", "C"),
    "C": ("B", "C", "A"),
}

# Bonuses:
#   A = Rock = 1
#   B = Paper = 2
#   C = Scissors = 3
choice_bonus = {
    "A": 1,
    "B": 2,
    "C": 3,
}

score = 0

for line in content.splitlines():
    x, y = line.split(" ")

    points_earned = pairs[y]
    points_earned += choice_bonus[outcome_map[x][int(points_earned / 3)]]

    score += points_earned

print("Total score: ", score)
