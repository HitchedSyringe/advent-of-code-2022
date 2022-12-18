"""
Copyright (C) 2021-present HitchedSyringe

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


import argparse
from pathlib import Path
from datetime import datetime

import requests


def get_session() -> str:
    with open(".session") as f:
        return f.read().strip()


def fetch_input(day_number: int) -> bytes:
    response = requests.get(
        f"https://adventofcode.com/2022/day/{day_number}/input",
        cookies={"session": get_session()}
    )
    response.raise_for_status()

    return response.content


_TEMPLATE: str = '''\
"""
Solution to Part {0} of Day {1} of Advent of Code {2}.
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

'''


def create_day(day_number: int, puzzle_input: bytes) -> None:
    path = Path(__file__).parent / format(day_number, ">02")
    path.mkdir(exist_ok=True)

    with open(path / "inputs.txt", "wb") as f:
        f.write(puzzle_input)

    for part, name in enumerate(("first.py", "second.py"), 1):
        fp = path / name
        fp.write_text(_TEMPLATE.format(part, day_number, datetime.now().year))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", type=int, help="The day number.", required=True)

    args = parser.parse_args()

    create_day(args.number, fetch_input(args.number))
