from tcod.ecs import Entity

from .directional import Directional
from ..position import Position


class Move(Directional):
    def execute(self, actor: Entity):
        actor.components[Position] += self.direction