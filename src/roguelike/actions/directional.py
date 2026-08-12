from ..action import Action
from ..vector import Vector


class Directional(Action):
    def __init__(self, direction: Vector) -> None:
        self.direction = direction