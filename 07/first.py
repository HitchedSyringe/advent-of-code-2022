"""
Solution to Part 1 of Day 7 of Advent of Code 2022.
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

from _shared import get_directory_sizes


TARGET_SIZE = 100000

path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

counts = get_directory_sizes(content)

total = sum(v for v in counts.values() if v <= TARGET_SIZE)

print("Sum of directories with size <= 100000: ", total)
