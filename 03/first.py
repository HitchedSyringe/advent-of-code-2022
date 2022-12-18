"""
Solution to Part 1 of Day 3 of Advent of Code 2022.
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


import string
from pathlib import Path


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

rucksacks = content.splitlines()

priorities = {c: i for i, c in enumerate(string.ascii_letters, 1)}

priority_sum = 0

for rucksack in rucksacks:
    half = len(rucksack) // 2

    first = rucksack[:half]
    second = rucksack[half:]

    intersecting = set(first).intersection(second)

    for item in intersecting:
        priority_sum += priorities[item]


print("The priority sum is: ", priority_sum)
