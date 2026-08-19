from collections.abc import Callable
import tcod.camera

from .. import g
from ..components import MapShape, Tiles
from ..tiles import TILE_DATA
from ..state import State
from ..action import Action
from ..actions import Move, Wait, Melee
from ..vector import Vector, vector_from_tuple
from ..components import Position, Graphic
from ..player_do import PlayerDo 


class ActionDispatch:
    def __call__(self):
        pass


class Bump(ActionDispatch):
    def __init__(self, direction: Vector):
        self.direction = direction

    def __call__(self):
        if not isinstance((melee_action := Melee(self.direction)).check(g.player), Melee.NoFighterThere):
            PlayerDo(melee_action)()
            return
        else:
            PlayerDo(Move(self.direction))()
            return


class Game(State):
    MOVE: Callable[[str], str] = lambda direction: 'move_'+direction
    WAIT = 'wait'

    def __init__(self):
        playerdo_actions: dict[str, Action] = {
            # State actions that use PlayerDo
            Game.WAIT: Wait(),
        }
        self.actions = {action_str: PlayerDo(action) for action_str, action in playerdo_actions.items()} | {
            # State actions that don't use PlayerDo
            Game.MOVE('north'): Bump(Vector(0,-1)),
            Game.MOVE('northeast'): Bump(Vector(1,-1)),
            Game.MOVE('east'): Bump(Vector(1,0)),
            Game.MOVE('southeast'): Bump(Vector(1,1)),
            Game.MOVE('south'): Bump(Vector(0,1)),
            Game.MOVE('southwest'): Bump(Vector(-1,1)),
            Game.MOVE('west'): Bump(Vector(-1,0)),
            Game.MOVE('northwest'): Bump(Vector(-1,-1)),
        }

    def update(self):
        g.simulation.advance()

    def draw(self):
        player_pos = g.player.components[Position]

        map_ = player_pos.map_
        map_shape = map_.components[MapShape]

        SCREEN_SHAPE = (30,30)

        player_ij = (player_pos.y, player_pos.x)
        camera_ij = tcod.camera.get_camera(SCREEN_SHAPE, player_ij)
        screen_slice, world_slice = tcod.camera.get_slices(SCREEN_SHAPE, map_shape, camera_ij)

        g.console.rgb[screen_slice] = TILE_DATA[map_.components[Tiles][world_slice]]["graphic"]

        rendered_offset = vector_from_tuple(camera_ij, ij=True)

        for entity in g.registry.Q.all_of(components=[Position, Graphic]):
            rendered_pos = entity.components[Position] - rendered_offset
            graphic = entity.components[Graphic]
            g.console.rgb[rendered_pos.y, rendered_pos.x] = graphic