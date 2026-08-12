from . import states
from . import state_id
from .state import State


STATE_FACTORIES: dict[str, type[State]] = {
    state_id.MAIN_MENU: states.MainMenu,
    state_id.GAME: states.Game,
}


class StateManager:
    def __init__(self, initial_state: State):
        self.stack: list[State] = [initial_state]

    @property
    def state(self):
        return self.stack[-1]

    def switch(self, state_id: str):
        self.stack = [STATE_FACTORIES[state_id]()]

    def push(self, state_id: str):
        self.stack.append(STATE_FACTORIES[state_id]())

    def pop(self):
        self.stack.pop()