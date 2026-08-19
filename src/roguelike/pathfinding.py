import tcod.path

from .components import Position, Tiles
from .tiles import TILE_DATA


def find_path_to(start: Position, end: Position) -> list[Position]:
    assert start.map_ == end.map_
    map_ = start.map_

    graph = tcod.path.SimpleGraph(
        cost=TILE_DATA["walkable"][map_.components[Tiles]], 
        cardinal=2,
        diagonal=3,
    )

    pf = tcod.path.Pathfinder(graph)

    pf.add_root((start.x, start.y))

    path = pf.path_to((end.x, end.y))

    return [Position(index[0], index[1], map_) for index in path[1:]]