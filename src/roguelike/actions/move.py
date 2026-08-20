from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from tcod.ecs import Entity
    import numpy as np

from .. import g
from ..action import Impossible
from .directional import Directional
from ..components import Position
from ..map_tools import get_tile
from ..entity_tools import get_name, get_entities_at
from ..tags import BlocksMovement
from .. import colors


class Move(Directional):
    @dataclass
    class BlockedByTile(Impossible):
        tile: np.ndarray

        def report(self):
            g.message_log.log(f"There's a {self.tile["name"]} in the way.", *colors.messages.ACTION_IMPOSSIBLE)

    @dataclass
    class BlockedByEntity(Impossible):
        entity: Entity

        def report(self):
            g.message_log.log(f"{get_name(self.entity)} is in the way.", *colors.messages.ACTION_IMPOSSIBLE)

    def check(self, actor: Entity):
        dest = self.dest(actor)
        dest_tile = get_tile(dest)
        if not dest_tile["walkable"]:
            return Move.BlockedByTile(dest_tile)
        elif (entities := get_entities_at(dest).all_of(tags=[BlocksMovement])):
            return Move.BlockedByEntity(list(entities)[0])

    def _execute(self, actor: Entity):
        actor.components[Position] += self.direction
