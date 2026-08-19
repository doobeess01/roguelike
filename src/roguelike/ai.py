from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity

import random

from . import g
from .action import Action
from .actions import Move, Melee, Wait
from .vector import Vector
from .pathfinding import find_path_to
from .components import Position
from .tags import IsHostile


def ai_choose_action(actor: Entity) -> Action:
    action: Action | None = None

    if IsHostile:
        actor_position = actor.components[Position]
        path_to_target = find_path_to(start=actor_position, end=g.player.components[Position])
        if path_to_target:
            next_position = path_to_target[0]
            direction = next_position - actor_position
            if len(path_to_target) == 1:  # Actor is adjacent to target
                action = Melee(direction)
            else:
                if Move(direction).check(actor) is None:
                    action = Move(direction)

    else:
        possible_movements = [Vector(x, y) for x in (-1,1) for y in (-1, 1)]

        while len(possible_movements) > 0:
            direction = random.choice(possible_movements)
            possible_movements.remove(direction)
            if Move(direction).check(actor) is None:  # Destination square is occupied by neither a blocking entity nor a wall
                action = Move(direction)

    if action is None:
        action = Wait()

    return action