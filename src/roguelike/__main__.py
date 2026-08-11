import tcod

import g


def handle_event(event: tcod.event.Event):
    if isinstance(event, tcod.event.Quit):
        raise SystemExit()


def draw():
    g.console.print(1, 1, "Hello, world!")
    g.console.print(3,3,"@")

    g.context.present(g.console)


def main() -> None:
    screen_width = 80
    screen_height = 50

    g.console = tcod.console.Console(screen_width, screen_height, order="F")

    tileset = tcod.tileset.load_tilesheet("assets/Alloy_curses_12x12.png", 16, 16, tcod.tileset.CHARMAP_CP437)

    with tcod.context.new(console=g.console, tileset=tileset, title="Roguelike", vsync=True) as g.context:
        while True:
            
            for event in tcod.event.wait():
                handle_event(event)


if __name__ == "__main__":
    main()