from enum import IntEnum

from . import g
from .event_bus import EventBus
from .events import Damage, Death
from .event_listeners import apply_damage, handle_death


class DamagePriorities(IntEnum):
    APPLY_DAMAGE = 0


class DeathPriorities(IntEnum):
    CLEAR_ENTITY = 0


def initialize_event_bus():
    g.event_bus = EventBus()

    g.event_bus.subscribe(Damage, apply_damage, priority=DamagePriorities.APPLY_DAMAGE)
    g.event_bus.subscribe(Death, handle_death, priority=DeathPriorities.CLEAR_ENTITY)