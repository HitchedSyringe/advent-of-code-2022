"""
Solution to Part 2 of Day 3 of Advent of Code 2022.
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


def chunk(iterable, *, size=1):
    length = len(iterable)

    for index in range(0, length, size):
        yield iterable[index:min(index + size, length)]

path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

rucksacks = content.splitlines()

priorities = {c: i for i, c in enumerate(string.ascii_letters, 1)}

priority_sum = 0

for first, second, third in chunk(rucksacks, size=3):
    intersecting = set(first).intersection(second, third)

    for item in intersecting:
        priority_sum += priorities[item]


print("The priority sum is: ", priority_sum)
