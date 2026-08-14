import tcod.ecs

from . import g
from .components import Position, Graphic
from .tags import IsIn, IsActor
from .map_init import generate_map


def initialize_world():
    g.registry = tcod.ecs.Registry()

    # Add player
    g.player = g.registry.new_entity(
        components={
            Position: Position(5,5),
            Graphic: Graphic(ord('@'),(255,255,255))
        }, 
        tags={IsActor}
    )

    # Add an NPC
    kobold = g.registry.new_entity(
        components={
            Position: Position(15,15),
            Graphic: Graphic(ord('K'),(240,120,30)),
        }, 
        tags={IsActor}
    )

    map_ = generate_map()
    g.player.relation_tag[IsIn] = map_
    kobold.relation_tag[IsIn] = map_