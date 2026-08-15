from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity

from . import g
from .components import Name, Position


def get_name(entity: Entity):
    return entity.components[Name]

def get_entities_at(position: Position):
    return g.registry.Q.all_of(tags=[position])