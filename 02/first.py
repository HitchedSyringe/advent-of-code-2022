
# Part 1 of Day 2 of Advent of Code 2022.

from pathlib import Path


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

# Opponent:
#   A = Rock
#   B = Paper
#   C = Scissors
# Player:
#   X = Rock
#   Y = Paper
#   Z = Scissors
winning_pairs = {
    "A": "Y",
    "B": "Z",
    "C": "X",
    "X": "B",
    "Y": "C",
    "Z": "A",
}

# Bonuses:
#   Rock = 1
#   Paper = 2
#   Scissors = 3
choice_bonus = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

score = 0

for line in content.splitlines():
    x, y = line.split(" ")

    score += choice_bonus[y]

    if winning_pairs[x] == y:  # Win
        score += 6
    elif winning_pairs[y] != x:  # Draw
        score += 3

print("Total score: ", score)
