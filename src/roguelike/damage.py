from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from tcod.ecs import Entity

from .components import HP
from .entity_tools import get_name


class Damage:
    def __init__(self, amount: int):
        self.amount = amount

    def get_modified_damage(self, target: Entity) -> tuple[int, dict[str, Any]]:
        return self.amount, {}

    def report(self, target: Entity, damage: int, info: dict[str, Any]):
        print(f'{get_name(target)} took {damage} damage!')

    def __call__(self, target: Entity):
        modified_amount, info = self.get_modified_damage(target)
        self.report(target, modified_amount, info)
        target.components[HP] -= modified_amount

