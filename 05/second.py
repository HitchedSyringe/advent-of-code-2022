"""
Solution to Part 2 of Day 5 of Advent of Code 2022.
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


# ...but this code is probably worse. I did my best for 1:05 AM brain.
from pathlib import Path


LAYERS = 8
COLUMNS = 9


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

lines = content.splitlines()

# Transpose the stacks into rows.
stacks = [[] for _ in range(COLUMNS)]

for layer in lines[:LAYERS]:
    for pos, i in enumerate(range(0, len(layer), 4)):
        if slot := layer[i:i + 4].strip("[ ]"):
            stacks[pos].insert(0, slot)

# Get important information from procedures.
procedures = [tuple(int(y) for y in x.split(" ") if y.isdigit()) for x in lines[LAYERS + 2:]]

# Stacks is in the following format:
# Column 1: ...
# Column 2: ...
# Column n: ...
for (num_crates, init_column_num, final_column_num) in procedures:
    init_column = stacks[init_column_num - 1]
    init_max = len(init_column)

    to_move = init_column[init_max - min(num_crates, init_max):init_max]
    stacks[final_column_num - 1].extend(to_move)

    for _ in range(len(to_move)):
        init_column.pop()


print("Stack tops:", "".join(stack[-1] for stack in stacks))
