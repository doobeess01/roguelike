from typing import TYPE_CHECKING
from dataclasses import dataclass

from ..event import Event

if TYPE_CHECKING:
    from tcod.ecs import Entity


@dataclass
class Death(Event):
    entity: Entity
