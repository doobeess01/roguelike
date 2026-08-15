from typing import Any

from tcod.ecs import Entity

from .physical import Physical
from ..entity_tools import get_name


class Melee(Physical):
    def __init__(self, amount: int, blame: Entity):
        super().__init__(amount)
        self.blame = blame
    def report(self, target: Entity, damage: int, info: dict[str, Any]):
        print(f'{get_name(self.blame)} hits {get_name(target)} for {damage} damage!')