from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity

from .components import Name


def die(entity: Entity):
    print(f'{entity.components[Name]} dies!')
    entity.clear()