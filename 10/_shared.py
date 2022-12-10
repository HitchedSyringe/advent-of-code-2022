
from collections.abc import Callable
from functools import wraps
from typing import Any, List, Tuple


def _cycle(*, cycle_cost: int) -> Callable[..., Callable[..., None]]:

    def inner(func: Callable[..., None]) -> Callable[..., None]:

        @wraps(func)
        def wrapped(cpu: "BaseCPU", *args: Any, **kwargs: Any) -> None:
            for _ in range(cycle_cost):
                cpu.cycles += 1
                cpu.execute_every_cycle()

            func(cpu, *args, **kwargs)

        return wrapped

    return inner


class BaseCPU:
    """Base CPU class which tracks the `X` register value and cycles.

    Attributes
    ----------
    X: :class:`int`
        The `X` register value.
    cycles: :class:`int`
        The number of cycles this CPU has undergone.
    """

    __slots__: Tuple[str, ...] = (
        "X",
        "cycles",
    )

    def __init__(self) -> None:
        self.X: int = 1
        self.cycles: int = 0

    def execute_every_cycle(self) -> None:
        """This method executes every cycle."""
        raise NotImplementedError

    @_cycle(cycle_cost=2)
    def addx(self, V: int) -> None:
        """Executes the `addx` command on the CPU.

        This changes the `X` register value by `V` and takes
        **2 cycles** to complete.

        Parameters
        ----------
        V: :class:`int`
            The value to change the `X` register value by.
        """
        self.X += V

    @_cycle(cycle_cost=1)
    def noop(self) -> None:
        """Executes the `noop` command on the CPU.

        This does nothing and takes **1 cycle** to complete.
        """
        pass


class SignalStrengthCPU(BaseCPU):
    """CPU class which tracks the signal strength at the desired cycles.

    These desired cycles are: #20, #60, #100, #140, #180, and #220

    Attributes
    ----------
    X: :class:`int`
        The `X` register value.
    cycles: :class:`int`
        The number of cycles this CPU has undergone.
    """

    __slots__: Tuple[str, ...] = (
        "_desired_signal_strengths",
    )

    _DESIRED_CYCLES: Tuple[int, ...] = (20, 60, 100, 140, 180, 220)

    def __init__(self) -> None:
        super().__init__()
        self._desired_signal_strengths: List[int] = []

    def execute_every_cycle(self) -> None:
        if self.cycles in self._DESIRED_CYCLES:
            self._desired_signal_strengths.append(self.X * self.cycles)

    @property
    def desired_signal_strengths_sum(self) -> int:
        """:class:`int`: Returns the sum of the desired cycles signal strengths."""
        return sum(self._desired_signal_strengths)


class DrawingCPU(BaseCPU):
    """CPU class which draws on a CRT.

    Attributes
    ----------
    X: :class:`int`
        The `X` register value.
    cycles: :class:`int`
        The number of cycles this CPU has undergone.
    """

    __slots__: Tuple[str, ...] = (
        "_line",
        "_canvas",
    )

    def __init__(self) -> None:
        super().__init__()

        self._line: str = ""
        self._canvas: List[str] = []

    @property
    def canvas(self) -> str:
        """:class:`str`: Returns the contents of the canvas."""
        return "\n".join(self._canvas)

    def execute_every_cycle(self) -> None:
        line = self._line
        line += "#" if self.X - 1 <= len(line) <= self.X + 1 else "."

        if len(line) == 40:
            self._canvas.append(line)
            self._line = ""
        else:
            self._line = line
