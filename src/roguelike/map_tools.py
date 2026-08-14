from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity

from .components import Tiles
from .tiles import TILE_DATA


def get_tile(map_: Entity, x: int, y: int):
    return TILE_DATA[map_.components[Tiles][y,x]]
