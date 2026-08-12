from . import g


class SwitchState:
    def __init__(self, state_id: str):
        self.state_id = state_id

    def __call__(self):
        g.state_manager.switch(self.state_id)


class PushState:
    def __init__(self, state_id: str):
        self.state_id = state_id

    def __call__(self):
        g.state_manager.push(self.state_id)


class PopState:
    def __call__(self):
        g.state_manager.pop()