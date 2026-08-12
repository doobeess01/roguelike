from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity


class Action:
    def __call__(self, actor: Entity):
        ...