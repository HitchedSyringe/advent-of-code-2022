"""
Solution to Part 1 of Day 8 of Advent of Code 2022.
Copyright (C) 2022-present HitchedSyringe

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


# I probably could've made it easier on myself had I used numpy. Oh well.
from pathlib import Path


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

lines = content.splitlines()

final_line = len(lines) - 1
final_tree = len(lines[0]) - 1

visible = 0

for i, line in enumerate(lines):
    if i in (0, final_line):
        visible += final_tree + 1
        continue

    for j, item in enumerate(line):
        if j in (0, final_tree):
            visible += 1
            continue

        item = int(item)

        row = list(map(int, line))
        column = [int(line[j]) for line in lines]

        # Left, Right, Top, Bottom
        directions = (row[:j], row[j + 1:], column[:i], column[i + 1:])

        if any(all(item > t for t in d) for d in directions):
            visible += 1


print("Visible trees:", visible)
