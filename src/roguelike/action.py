from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod.ecs import Entity

from . import g


class Impossible:
    '''Base class for action *attempt* failures (for example, a missed melee attack would NOT return Impossible, while a melee attack to a nonexistent target would)'''
    pass


class Action:
    def check(self, actor: Entity) -> Impossible | None:
        ...

    def _execute(self, actor: Entity):
        ...

    def __call__(self, actor: Entity) -> Impossible | None:
        if (failure := self.check(actor)) is not None:
            return failure
        
        self._execute(actor)
        g.event_bus.process()

        
        