from tcod.ecs import Entity

from ..action import ActionCheckFeedback, Success, Impossible

from .directional import Directional
from ..components import Position
from ..tags import IsIn
from ..map_tools import get_tile


class Move(Directional):
    def check(self, actor: Entity) -> ActionCheckFeedback:
        map_ = actor.relation_tag[IsIn]
        dest = actor.components[Position] + self.direction
        if get_tile(map_, dest.x, dest.y)["walkable"]:
            return Success()
        return Impossible("You can't walk through walls.")

    def execute(self, actor: Entity):
        actor.components[Position] += self.direction