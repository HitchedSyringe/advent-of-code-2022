
# Part 2 of Day 11 of Advent of Code 2022.

from pathlib import Path

from _shared import play_keep_away


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

monkey_business = play_keep_away(content, rounds=10000, relief=False)

print("Monkey business level: ", monkey_business)
