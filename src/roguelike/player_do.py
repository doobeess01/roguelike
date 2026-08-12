from typing import TYPE_CHECKING
from collections.abc import Callable

if TYPE_CHECKING:
    from tcod.ecs import Entity

from . import g


class PlayerDo:
    def __init__(self, player_action: Callable[[Entity], None]):
        self.player_action = player_action
    def __call__(self):
        self.player_action(g.player)