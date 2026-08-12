import tcod.ecs

from . import g
from .position import Position


def initialize_world():
    g.registry = tcod.ecs.Registry()

    g.player = g.registry.new_entity(components={Position: Position(5,5)})