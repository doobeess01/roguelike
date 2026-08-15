from collections.abc import Callable

from .. import g
from ..components import MapShape, Tiles
from ..tiles import TILE_DATA
from ..state import State
from ..action import Action
from ..actions import Move, Wait, Melee
from ..vector import Vector
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

    def draw(self):
        map_ = g.player.components[Position].map_
        map_shape = map_.components[MapShape]
        g.console.rgb[:map_shape.height, :map_shape.width] = TILE_DATA[map_.components[Tiles]]["graphic"]

        for entity in g.registry.Q.all_of(components=[Position, Graphic]):
            pos = entity.components[Position]
            graphic = entity.components[Graphic]
            g.console.rgb[pos.y, pos.x] = graphic