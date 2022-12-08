
# Part 2 of Day 8 of Advent of Code 2022.
# Not too proud of this one either...

import operator
from functools import reduce
from pathlib import Path


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

lines = content.splitlines()

scenic_scores = []

for i, line in enumerate(lines):
    for j, item in enumerate(line):
        item = int(item)

        row = list(map(int, line))
        column = [int(line[j]) for line in lines]

        # Need to reverse left and top views since we're scanning
        # from the POV of the selected tree.
        directions = (
            reversed(row[:j]),     # Left POV
            row[j + 1:],           # Right POV
            reversed(column[:i]),  # Top POV
            column[i + 1:],        # Bottom POV
        )

        dir_scores = []

        for d in directions:
            dir_score = 0

            for t in d:
                dir_score += 1
                if t >= item:
                    break

            dir_scores.append(dir_score)

        scenic_scores.append(reduce(operator.mul, dir_scores))


print("Highest scenic score: ", max(scenic_scores))
