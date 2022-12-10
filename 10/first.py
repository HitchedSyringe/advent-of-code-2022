
# Part 1 of Day 10 of Advent of Code 2022.

from pathlib import Path

from _shared import SignalStrengthCPU


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

lines = content.splitlines()
cpu = SignalStrengthCPU()

for line in lines:
    command, _, argument = line.partition(" ")

    if command == "addx":
        cpu.addx(int(argument))
    elif command == "noop":
        cpu.noop()


print("Signal strength sum: ", cpu.desired_signal_strengths_sum)
