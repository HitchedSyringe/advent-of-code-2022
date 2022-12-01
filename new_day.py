import argparse
from pathlib import Path

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


template: str = """
# Part {0} of Day {1} of Advent of Code 2022.

from pathlib import Path


with open(Path(__file__).parent / "inputs.txt") as f:
    pass

"""


def create_day(day_number: int, puzzle_input: bytes) -> None:
    path = Path(__file__).parent / format(day_number, ">02")
    path.mkdir(exist_ok=True)

    with open(path / "inputs.txt", "wb") as f:
        f.write(puzzle_input)

    for part, name in enumerate(("first.py", "second.py"), 1):
        with open(path / name, "w") as f:
            f.write(template.format(part, day_number))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", type=int, help="Advent of Code puzzle day number.", required=True)

    args = parser.parse_args()

    create_day(args.number, fetch_input(args.number))
