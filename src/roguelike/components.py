from typing import Any, Final, NamedTuple

import numpy as np

from .vector import Vector


class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    def __add__(self, other: Any):
        if isinstance(other, Vector):
            return Position(self.x+other.x, self.y+other.y)
        return NotImplemented
    def __sub__(self, other: Any):
        if isinstance(other, Vector):
            return Position(self.x-other.x, self.y-other.y)
        return NotImplemented


class Graphic(NamedTuple):
    ch: int
    fg: tuple[int, int, int] = (255,255,255)
    bg: tuple[int, int, int] = (0,0,0)


class MapShape(NamedTuple):
    """Map shape tuple."""
    height: int
    width: int


Tiles: Final = ('Tiles', np.ndarray)