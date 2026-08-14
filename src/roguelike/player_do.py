from . import g
from .action import Action, Impossible
from .simulation import handle_npc_turns


class PlayerDo:
    def __init__(self, player_action: Action):
        self.player_action = player_action

    def __call__(self):
        feedback = self.player_action(g.player)
        if isinstance(feedback, Impossible):
            print(feedback.message)

        handle_npc_turns()