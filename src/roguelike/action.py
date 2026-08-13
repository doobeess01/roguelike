from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity


class ActionCheckFeedback:
    pass


class Success(ActionCheckFeedback):
    pass


class Impossible(ActionCheckFeedback):
    def __init__(self, message: str):
        self.message = message


class Action:
    def __call__(self, actor: Entity):
        if isinstance(feedback := self.check(actor), Success):
            self.execute(actor)
        return feedback
    
    def check(self, actor: Entity) -> ActionCheckFeedback:
        '''Check whether the action is currently possible to complete. Returns an ActionCheckFeedback object.'''
        return Success()
    
    def execute(self, actor: Entity):
        ...