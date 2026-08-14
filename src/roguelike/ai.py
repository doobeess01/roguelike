from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity

import random

from .action import Action
from .actions import Move, Wait
from .vector import Vector
from .components import Position, Tiles
from .tags import IsIn
from .tiles import TILE_DATA


def ai_choose_action(actor: Entity) -> Action:
    action: Action | None = None

    map_ = actor.relation_tag[IsIn]
    possible_movements = [Vector(x, y) for x in (-1,1) for y in (-1, 1)]

    while action is None:
        direction = random.choice(possible_movements)
        possible_movements.remove(direction)
        dest = actor.components[Position] + direction
        if TILE_DATA["walkable"][map_.components[Tiles][dest.y, dest.x]]:
            action = Move(direction)
        elif len(possible_movements) == 0:
            action = Wait()

    return action