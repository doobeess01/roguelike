import tcod

from . import g
from .state_manager import StateManager
from . import states

from .handle_event import handle_event


def draw():
    g.console.clear()
    g.state_manager.state.draw()
    g.context.present(g.console)


def main() -> None:
    screen_width = 80
    screen_height = 50

    g.console = tcod.console.Console(screen_width, screen_height)

    tileset = tcod.tileset.load_tilesheet("assets/Alloy_curses_12x12.png", 16, 16, tcod.tileset.CHARMAP_CP437)

    g.state_manager = StateManager(states.MainMenu())

    with tcod.context.new(console=g.console, tileset=tileset, title="Roguelike", vsync=True) as g.context:
        while True:
            
            for event in tcod.event.wait():
                handle_event(event)

            draw()


if __name__ == "__main__":
    main()