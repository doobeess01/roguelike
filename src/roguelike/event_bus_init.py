from enum import IntEnum

from . import g
from .event_bus import EventBus
from .events import Damage, Death
from .event_listeners import damage, death


class Priorities(IntEnum):
    BEFORE = -10
    DURING = 0
    AFTER = 10


def initialize_event_bus():
    g.event_bus = EventBus()

    g.event_bus.subscribe(Damage, damage.apply_damage, priority=Priorities.DURING)

    g.event_bus.subscribe(Death, death.report_death, priority=Priorities.DURING)
    g.event_bus.subscribe(Death, death.clear_dead_entity, priority=Priorities.AFTER)