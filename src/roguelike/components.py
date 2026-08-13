from typing import Final, NamedTuple

import numpy as np


class MapShape(NamedTuple):
    """Map shape tuple."""
    height: int
    width: int


Tiles: Final = ('Tiles', np.ndarray)