from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity

import random

from .action import Action
from .actions import Move, Wait
from .vector import Vector
from .components import Position
from .tags import IsIn
from .map_tools import get_tile


def ai_choose_action(actor: Entity) -> Action:
    action: Action | None = None

    map_ = actor.relation_tag[IsIn]
    possible_movements = [Vector(x, y) for x in (-1,1) for y in (-1, 1)]

    while action is None:
        direction = random.choice(possible_movements)
        possible_movements.remove(direction)
        dest = actor.components[Position] + direction
        if get_tile(map_, dest.x, dest.y)["walkable"]:
            action = Move(direction)
        elif len(possible_movements) == 0:
            action = Wait()

    return action