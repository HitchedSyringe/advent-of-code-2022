"""
Solution to Part 1 of Day 4 of Advent of Code 2022.
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


from pathlib import Path


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

pairs = content.splitlines()

full_overlaps = 0

def as_range(assignment):
    first, last = assignment.split("-")
    return range(int(first), int(last) + 1)

for pair in pairs:
    first, second = pair.split(",")

    first = set(as_range(first))
    second = set(as_range(second))

    if first.issubset(second) or second.issubset(first):
        full_overlaps += 1


print("Full overlaps: ", full_overlaps)
