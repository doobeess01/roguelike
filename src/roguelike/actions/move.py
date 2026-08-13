from tcod.ecs import Entity

from ..action import ActionCheckFeedback, Success, Impossible

from .directional import Directional
from ..position import Position
from ..components import Tiles
from ..tags import IsIn
from ..tiles import TILE_DATA


class Move(Directional):
    def check(self, actor: Entity) -> ActionCheckFeedback:
        tiles = actor.relation_tag[IsIn].components[Tiles]
        dest = actor.components[Position] + self.direction
        if TILE_DATA["walkable"][tiles[dest.y,dest.x]]:
            return Success()
        return Impossible("You can't walk through walls.")

    def execute(self, actor: Entity):
        actor.components[Position] += self.direction