from typing import TYPE_CHECKING

from .tags import IsPlayer

if TYPE_CHECKING:
    import tcod
    import tcod.ecs
    from .state_manager import StateManager
    from .event_bus import EventBus
    from .simulation import Simulation
    from .message_log import MessageLog


console: tcod.console.Console
context: tcod.context.Context

state_manager: StateManager

registry: tcod.ecs.Registry
def player() -> tcod.ecs.Entity:
    for entity in registry.Q.all_of(tags=[IsPlayer]):
        return entity
    else:
        raise RuntimeError('No entity with IsPlayer tag!')

event_bus: EventBus

simulation: Simulation

message_log: MessageLog