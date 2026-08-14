from collections.abc import Callable

from .. import g
from ..tags import IsIn
from ..components import MapShape, Tiles
from ..tiles import TILE_DATA
from ..state import State
from ..action import Action
from ..actions import Move, Wait
from ..vector import Vector
from ..components import Position, Graphic
from ..player_do import PlayerDo 


class Game(State):
    MOVE: Callable[[str], str] = lambda direction: 'move_'+direction
    WAIT = 'wait'

    def __init__(self):
        player_actions: dict[str, Action] = {
            # State actions that are player actions
            Game.MOVE('north'): Move(Vector(0,-1)),
            Game.MOVE('northeast'): Move(Vector(1,-1)),
            Game.MOVE('east'): Move(Vector(1,0)),
            Game.MOVE('southeast'): Move(Vector(1,1)),
            Game.MOVE('south'): Move(Vector(0,1)),
            Game.MOVE('southwest'): Move(Vector(-1,1)),
            Game.MOVE('west'): Move(Vector(-1,0)),
            Game.MOVE('northwest'): Move(Vector(-1,-1)),
            Game.WAIT: Wait(),
        }
        self.actions = {action_str: PlayerDo(action) for action_str, action in player_actions.items()} | {
            # State actions that aren't (at least directly) player actions
            # None implemented yet.
        }

    def draw(self):
        map_ = g.player.relation_tag[IsIn]
        map_shape = map_.components[MapShape]
        g.console.rgb[:map_shape.height, :map_shape.width] = TILE_DATA[map_.components[Tiles]]["graphic"]

        for entity in g.registry.Q.all_of(components=[Position, Graphic]):
            pos = entity.components[Position]
            graphic = entity.components[Graphic]
            g.console.rgb[pos.y, pos.x] = graphic