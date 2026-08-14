from collections.abc import Callable


class State:
    actions: dict[str, Callable[[], None]]

    def draw(self):
        ...

    def execute_action(self, action_str: str):
        if self.actions.get(action_str, False):
            self.actions[action_str]()