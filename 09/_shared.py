"""
Shared components for Day 9 solutions.
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


import math
from typing import Dict, List, Tuple


_DIRECTION_MAP: Dict[str, Tuple[int, int]] = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}


def _move_head(head: Tuple[int, int], direction: str) -> Tuple[int, int]:
    x_sign, y_sign = _DIRECTION_MAP[direction]
    return (head[0] + x_sign, head[1] + y_sign)


def _follow(leader: Tuple[int, int], follower: Tuple[int, int]) -> Tuple[int, int]:
    follower_x, follower_y = follower

    dx = leader[0] - follower_x
    dy = leader[1] - follower_y

    # If |dx| == 2 and |dy| == 0, move tail 1 on x axis.
    # If |dx| == 0 and |dy| == 2, move tail 1 on y axis.
    # If |dx| == 2 or |dy| == 2, move tail 1 on x and 1 on y axis.

    if abs(dx) > 1 or abs(dy) > 1:
        follower_x += (0 if dx == 0 else int(math.copysign(1, dx)))
        follower_y += (0 if dy == 0 else int(math.copysign(1, dy)))

    return (follower_x, follower_y)


def get_unique_tail_position_count(input_lines: List[str], knots_amount: int) -> int:
    """Gets the number of unique positions the tail of the rope has been.

    Parameters
    ----------
    input_lines: List[:class:`str`]
        The lines from the given input.
    knots_amount: :class:`int`
        The number of knots to track.

    Returns
    -------
    :class:`int`
        The number of unique positions the tail of the rope has been
    """
    knots_pos: List[Tuple[int, int]] = [(0, 0)] * knots_amount

    tail_visited = {knots_pos[-1]}

    for line in input_lines:
        direction, steps = line.split(" ")

        for _ in range(int(steps)):
            knots_pos[0] = _move_head(knots_pos[0], direction)

            for i in range(1, knots_amount):
                knots_pos[i] = _follow(knots_pos[i - 1], knots_pos[i])

            tail_visited.add(knots_pos[-1])

    return len(tail_visited)
