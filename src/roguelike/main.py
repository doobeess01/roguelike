import tcod

from . import g
from .state_manager import StateManager
from . import states
from .handle_tcod_event import handle_tcod_event
from .event_bus_init import get_event_bus
from .world_init import initialize_world


SCREEN_WIDTH, SCREEN_HEIGHT = 80, 50


def draw():
    g.console.clear()
    g.state_manager.state.draw()
    g.context.present(g.console)


def main() -> None:
    g.console = tcod.console.Console(SCREEN_WIDTH, SCREEN_HEIGHT)

    tileset = tcod.tileset.load_tilesheet("src/roguelike/assets/Alloy_curses_12x12.png", 16, 16, tcod.tileset.CHARMAP_CP437)

    g.state_manager = StateManager(states.MainMenu())

    g.event_bus = get_event_bus() # Sets g.event_bus
    initialize_world() # Sets g.registry


    with tcod.context.new(console=g.console, tileset=tileset, title="Roguelike", vsync=True) as g.context:
        while True:
            
            for event in tcod.event.wait():
                handle_tcod_event(event)

            g.state_manager.state.update()
            draw()


if __name__ == "__main__":
    main()