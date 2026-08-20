import tcod.camera

from .. import g
from ..components import MapShape, Tiles
from ..tiles import TILE_DATA

from ..vector import vector_from_tuple
from ..components import Position, Graphic


def main_game_render():
    screen_shape = (39, 60)
    render_map(screen_shape)  # Renders at 0-38 x, 0-59 y with C order
    render_message_log(0, 40, 10)
    g.console.print(0,39,'─'*80)


def render_message_log(x: int, y: int, rows: int):
    messages = g.message_log.get_messages(rows)
    for i, message in enumerate(messages):
        message.text_with_count.print(x, y+i)


def render_map(screen_shape: tuple[int, int]):
    # Render tiles

    player_pos = g.player().components[Position]

    map_ = player_pos.map_
    map_shape = map_.components[MapShape]

    player_ij = player_pos.ij
    camera_ij = tcod.camera.get_camera(screen_shape, player_ij)
    screen_slice, world_slice = tcod.camera.get_slices(screen_shape, map_shape, camera_ij)

    g.console.rgb[screen_slice] = TILE_DATA[map_.components[Tiles][world_slice]]["graphic"]

    # Render entities

    rendered_offset = vector_from_tuple(camera_ij, ij=True)

    for entity in g.registry.Q.all_of(components=[Position, Graphic]):
        rendered_pos = entity.components[Position] - rendered_offset
        graphic = entity.components[Graphic]
        g.console.rgb[rendered_pos.y, rendered_pos.x] = graphic