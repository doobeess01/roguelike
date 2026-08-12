from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import tcod
    import tcod.ecs
    from .state_manager import StateManager

console: tcod.console.Console
context: tcod.context.Context

state_manager: StateManager

registry: tcod.ecs.Registry
player: tcod.ecs.Entity