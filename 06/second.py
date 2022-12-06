
# Part 2 of Day 6 of Advent of Code 2022.

from pathlib import Path

from _shared import find_start_marker


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

start_of_message = find_start_marker(content, window_size=14)

print("Message start marker position: ", start_of_message)
