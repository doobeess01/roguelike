from typing import TYPE_CHECKING

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
player: tcod.ecs.Entity

event_bus: EventBus

simulation: Simulation

message_log: MessageLog