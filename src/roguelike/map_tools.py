from .components import Position, Tiles
from .tiles import TILE_DATA


def get_tile(position: Position):
    return TILE_DATA[position.map_.components[Tiles][position.y,position.x]]
