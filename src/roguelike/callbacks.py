from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity

from tcod.ecs import callbacks

from .components import Position, HP
from .combat_tools import die


def on_position_changed(entity: Entity, old: Position | None, new: Position | None):
    if old is not None:
        entity.tags.remove(old)
        entity.tags.remove(old.map_)
    if new is not None:
        entity.tags.add(new)
        entity.tags.add(new.map_)


def on_hp_changed(entity: Entity, old: int | None, new: int | None):
    if new is not None:
        if new <= 0:
            die(entity)


def register_all():
    callbacks.register_component_changed(component=Position)(on_position_changed)
    callbacks.register_component_changed(component=HP)(on_hp_changed)