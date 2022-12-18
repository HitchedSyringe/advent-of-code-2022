"""
Shared components for Day 7 solutions.
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


from collections import Counter


def get_directory_sizes(puzzle_input: str) -> Counter[str]:
    """Parses the given puzzle input and returns the sizes of each directory.

    Parameters
    ----------
    puzzle_input: :class:`str`
        The puzzle input containing the commands run.

    Returns
    -------
    :class:`collections.Counter`
        A counter containing a mapping of the directories and their sizes.
    """
    lines = puzzle_input.splitlines()

    counts = Counter()
    current_path = []

    for line in lines:
        line = line.lstrip("$ ")

        if line.startswith("cd"):
            command, _, selected_folder = line.partition(" ")

            if selected_folder == "/":
                current_path.clear()
            elif selected_folder == "..":
                if current_path:
                    current_path.pop()
            else:
                current_path.append(selected_folder)

            continue

        if not line.startswith(("dir", "ls")):
            filesize_str, _, _ = line.partition(" ")
            filesize = int(filesize_str)

            counts["/" + "/".join(current_path)] += filesize

            for i in range(len(current_path)):
                counts["/" + "/".join(current_path[:i])] += filesize

    return counts
