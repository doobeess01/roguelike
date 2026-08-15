from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity

import random

from .action import Action
from .actions import Move, Wait
from .vector import Vector


def ai_choose_action(actor: Entity) -> Action:
    action: Action | None = None

    possible_movements = [Vector(x, y) for x in (-1,1) for y in (-1, 1)]

    while action is None:
        direction = random.choice(possible_movements)
        possible_movements.remove(direction)
        if Move(direction).check(actor) is None:  # Destination square is occupied by neither a blocking entity nor a wall
            action = Move(direction)
        elif len(possible_movements) == 0:
            action = Wait()

    return action