import tcod.ecs

from . import g
from .position import Position
from .tags import IsIn
from .map_init import generate_map


def initialize_world():
    g.registry = tcod.ecs.Registry()

    g.player = g.registry.new_entity(components={Position: Position(5,5)})
    map_ = generate_map()
    g.player.relation_tag[IsIn] = map_
