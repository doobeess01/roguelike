from collections.abc import Callable

from .. import g
from ..state import State
from ..action import Action
from ..actions import Move, Wait, Melee
from ..vector import Vector
from ..player_do import PlayerDo 
from .rendering import main_game_render


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
        main_game_render()