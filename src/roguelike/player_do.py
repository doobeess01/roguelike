from . import g
from .action import Action, Impossible
from .simulation import handle_npc_turns


class PlayerDo:
    def __init__(self, player_action: Action):
        self.player_action = player_action

    def __call__(self):
        failure: Impossible | None = self.player_action(g.player)
        if failure is not None:
            failure.report()

        handle_npc_turns()