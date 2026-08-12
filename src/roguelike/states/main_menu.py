from .. import g
from ..state import State
from .. import state_id
from ..state_transitions import SwitchState


class MainMenu(State):
    BEGIN = 'begin'

    def __init__(self):
        self.actions = {
            self.BEGIN: SwitchState(state_id.GAME)
        }

    def draw(self):
        g.console.print(1,1,'Placeholder Main Menu State. Press ENTER to go the the game...')