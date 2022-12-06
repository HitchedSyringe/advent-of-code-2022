
# Part 1 of Day 6 of Advent of Code 2022.

from pathlib import Path

from _shared import find_start_marker


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

start_of_packet = find_start_marker(content, window_size=4)

print("Packet start marker position: ", start_of_packet)
