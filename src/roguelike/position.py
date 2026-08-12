from typing import Any

from .vector import Vector


class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    def __add__(self, other: Any):
        if isinstance(other, Vector):
            return Position(self.x+other.x, self.y+other.y)
    def __sub__(self, other: Any):
        if isinstance(other, Vector):
            return Position(self.x-other.x, self.y-other.y)
