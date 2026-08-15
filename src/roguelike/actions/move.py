from tcod.ecs import Entity

from ..action import Impossible
from .directional import Directional
from ..components import Position
from ..map_tools import get_tile
from ..entity_tools import get_entities_at
from ..tags import BlocksMovement


class Move(Directional):
    class BlockedByTile(Impossible): pass
    class BlockedByEntity(Impossible): pass

    def check(self, actor: Entity):
        dest = actor.components[Position] + self.direction
        if not get_tile(dest)["walkable"]:
            return Move.BlockedByTile()
        elif get_entities_at(dest).all_of(tags=[BlocksMovement]):
            return Move.BlockedByEntity()

    def _execute(self, actor: Entity):
        actor.components[Position] += self.direction
