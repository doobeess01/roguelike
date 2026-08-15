from typing import TYPE_CHECKING, Any, Final, NamedTuple

if TYPE_CHECKING:
    from tcod.ecs import Entity

import numpy as np

from .vector import Vector


class Position:
    def __init__(self, x: int, y: int, map_: Entity) -> None:
        self.x = x
        self.y = y
        self.map_ = map_
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y and self.map_ == other.map_
        return False
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.map_))
    def __add__(self, other: Any):
        if isinstance(other, Vector):
            return Position(self.x+other.x, self.y+other.y, self.map_)
        return NotImplemented
    def __sub__(self, other: Any):
        if isinstance(other, Vector):
            return Position(self.x-other.x, self.y-other.y, self.map_)
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

Name: Final = ('Name', str)

HP: Final = ('HP', int)
Attack: Final = ('Attack', int)