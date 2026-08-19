from . import g
from .action import Action


class PlayerDo:
    def __init__(self, player_action: Action):
        self.player_action = player_action

    def __call__(self):
        if (failure := self.player_action.check(g.player)) is not None:
            failure.report()
        else:
            g.simulation.provide_action(self.player_action)