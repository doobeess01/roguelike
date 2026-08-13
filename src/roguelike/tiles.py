"""Tile definitions."""

from __future__ import annotations

from typing import NamedTuple

import numpy as np

GRAPHIC_DTYPE = np.dtype(
    [
        ("ch", np.intc),
        ("fg", "3B"),
        ("bg", "3B"),
    ]
)
"""Tile graphic data type."""

TILE_DTYPE = np.dtype(
    [
        ("name", np.object_),
        ("graphic", GRAPHIC_DTYPE),
        ("walkable", np.bool),
        ("transparent", np.bool),
    ]
)
"""Tile data type."""


class TileGraphic(NamedTuple):
    ch: int
    fg: tuple[int, int, int] = (255, 255, 255)
    bg: tuple[int, int, int] = (0, 0, 0)

class NewTile(NamedTuple):
    """Helper class for new tiles."""

    name: str
    graphic: TileGraphic
    walkable: bool = False
    transparent: bool = False


TILE_DATA = np.array(
    [
        NewTile(name="wall", graphic=TileGraphic(ch=(ord("#")), fg=(255, 255, 255), bg=(0, 0, 0)), walkable=False, transparent=False),
        NewTile(name="floor", graphic=TileGraphic(ch=(ord(".")), fg=(255, 255, 255), bg=(0, 0, 0)), walkable=True, transparent=True),
    ],
    dtype=TILE_DTYPE,
)
"""Tile database."""


TILE_ID = {name: i for i, name in enumerate(TILE_DATA["name"])}