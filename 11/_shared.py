
import math
import operator
from itertools import zip_longest
from collections.abc import Callable, Iterable
from typing import Any, Dict, List, Tuple


_OPERATORS: Dict[str, Callable[[int, int], int]] = {
    "+": operator.add,
    "*": operator.mul,
}


# itertools recipe from https://docs.python.org/3/library/itertools.html
def _grouper(iterable: Iterable, *, chunk_size: int) -> Iterable[Any]:
    args = [iter(iterable)] * chunk_size
    return zip_longest(*args, fillvalue=None)


def play_keep_away(data: str, *, rounds: int, relief: bool) -> int:
    """Plays n amount of rounds of \"keep away\".

    Parameters
    ----------
    data: :class:`str`
        The data to build the monkeys from.
    rounds: :class:`int`
        The amount of rounds to play.
    relief: :class:`bool`
        Whether or not to factor relief after item inspection.

    Returns
    -------
    :class:`int`
        The level of monkey business that occurred this game.
    """
    chunks = _grouper(data.splitlines(), chunk_size=7)
    monkeys = []

    for _, items, operation, test, true_case, false_case, _ in chunks:
        test_number = int(test.replace("Test: divisible by ", "").strip())
        _Monkey._MOD_CONST *= test_number

        items = [int(i) for i in items.replace("Starting items: ", "").strip().split(", ")]
        true_case = int(true_case.replace("If true: throw to monkey ", "").strip())
        false_case = int(false_case.replace("If false: throw to monkey ", "").strip())

        operation = operation.replace("Operation: new = old ", "").strip()
        operator_str, _, operand = operation.partition(" ")
        operator_func = _OPERATORS[operator_str]

        monke = _Monkey(items, true_case, false_case, operator_func, operand, test_number)
        monkeys.append(monke)

    for _ in range(rounds):
        for monke in monkeys:
            while monke.items:
                monke.inspect_current_item(relief=relief)

                receiver_id = monke.get_receiver_id()
                monkeys[receiver_id].items.append(monke.items.pop(0))

    inspected_counts = sorted((m.inspected_items for m in monkeys), reverse=True)

    return operator.mul(*inspected_counts[:2])


class _Monkey:

    __slots__: Tuple[str, ...] = (
        "items",
        "inspected_items",
        "_when_true",
        "_when_false",
        "_test_number",
        "_operator",
        "_operand",
    )

    _MOD_CONST: int = 1

    def __init__(
        self,
        items: List[int],
        receiver_when_true: int,
        receiver_when_false: int,
        operator: Callable[[int, int], int],
        operand: str,
        test_number: int,
    ) -> None:
        self.items: List[int] = items

        self._when_true: int = receiver_when_true
        self._when_false: int = receiver_when_false

        self._test_number: int = test_number

        self._operator: Callable[[int, int], int] = operator
        self._operand: str = operand

        self.inspected_items: int = 0

    def inspect_current_item(self, *, relief: bool) -> None:
        current_item = self.items[0]
        operand = self._operand

        other = int(operand) if operand != "old" else current_item

        # This is necessary to keep worry levels manageable, especially
        # in part 2. Otherwise, you'd need a NASA super computer to run
        # this simulation. I'm not a mathematician, but I'll attempt to
        # explain this the best of my ability given what I've read thus
        # far. I'll include my references and "see alsos" at the end of
        # this.
        #
        # This works because of the following properties of modulo:
        #
        # -> If a == b % n and b == c % n, then a == c % n.
        # -> If a == b % n, then...
        #    -> (a + k) == (b + k) % n for any integer k.
        #    -> ka == kb % kn for any integer k.
        #
        # The above implies that modulo congruence is preserved for any
        # multiplication or addition operations, which is perfect since
        # our operations only involve addition or multiplication.
        #
        # References:
        # - https://aoc.just2good.co.uk/2022/11
        # - https://en.wikipedia.org/wiki/Modular_arithmetic#Properties
        #
        # See also (better explanation with examples):
        # - https://github.com/blemelin/advent-of-code-2022/blob/main/src/day11.rs
        new_item = self._operator(current_item, other) % self._MOD_CONST

        if relief:
            new_item = math.floor(new_item / 3)

        self.items[0] = new_item
        self.inspected_items += 1

    def get_receiver_id(self) -> int:
        condition = self.items[0] % self._test_number == 0
        return self._when_true if condition else self._when_false
