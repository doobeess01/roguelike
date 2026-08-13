import numpy as np

from . import g
from .components import MapShape, Tiles
from .tiles import TILE_ID

MAP_WIDTH: int = 30
MAP_HEIGHT: int = 30


def generate_map():
    shape = MapShape(height=MAP_HEIGHT, width=MAP_WIDTH)

    tiles = np.full(shape, TILE_ID['wall'], dtype=np.uint8)
    tiles[1:-1, 1:-1] = TILE_ID['floor']


    map_ = g.registry.new_entity(
        components={
            MapShape: shape,
            Tiles: tiles,
        }
    )

    return map_
