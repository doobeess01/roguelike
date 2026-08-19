from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity
    from ..vector import Vector

from ..action import Action
from ..components import Position


class Directional(Action):
    def __init__(self, direction: Vector) -> None:
        self.direction = direction

    def dest(self, actor: Entity):
        return actor.components[Position] + self.direction