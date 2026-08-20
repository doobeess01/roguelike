from tcod.ecs import Entity
from collections import deque
from collections.abc import Iterable

from .tags import IsPlayer
from .ai import ai_choose_action
from .action import Action


class Simulation:
    def __init__(self, schedule: Iterable[Entity] | None = None):
        self.schedule: deque[Entity] = deque() if schedule is None else deque(schedule)
        self.pending_action: Action | None = None

    def advance(self):
        while True:
            actor = self.schedule.popleft()
            action: Action | None = None
            if self._needs_external_input(actor):
                if self.pending_action is not None:
                    action = self.pending_action
                    self.pending_action = None
                else:
                    self.schedule.appendleft(actor)
                    return
            else:
                action = ai_choose_action(actor)

            self._execute(actor, action)
            self.schedule.append(actor)

    def add_actor(self, actor: Entity):
        self.schedule.append(actor)

    def remove_actor(self, actor: Entity):
        self.schedule.remove(actor)

    def provide_action(self, action: Action):
        self.pending_action = action

    def _execute(self, actor: Entity, action: Action):
        action(actor)

    def _needs_external_input(self, actor: Entity):
        return IsPlayer in actor.tags
