from collections.abc import Callable

from .. import g
from ..state import State
from ..action import Action
from ..actions import Move, Wait
from ..vector import Vector
from ..position import Position
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
        player_position = g.player.components[Position]
        g.console.print(player_position.x, player_position.y, '@')