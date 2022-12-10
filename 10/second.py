
# Part 2 of Day 10 of Advent of Code 2022.

from pathlib import Path

from _shared import DrawingCPU


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

content = path.read_text()

lines = content.splitlines()
cpu = DrawingCPU()

for line in lines:
    command, _, argument = line.partition(" ")

    if command == "addx":
        cpu.addx(int(argument))
    elif command == "noop":
        cpu.noop()

print("Canvas:\n", cpu.canvas)
