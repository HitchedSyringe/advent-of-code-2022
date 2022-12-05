
# Part 2 of Day 5 of Advent of Code 2022.
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
