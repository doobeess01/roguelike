import tcod.constants

from .. import g
from .menu import Menu, MenuOption
from ..text import Text
from .. import state_id
from ..state_transitions import SwitchState


class MainMenu(Menu):
    def __init__(self):
        options: list[MenuOption] = [
            MenuOption(Text('Start Game'), SwitchState(state_id.GAME)),
            MenuOption(Text('Quit'), exit),
        ]
        super().__init__(options)

    def draw(self):
        g.console.print(0,2,'-- I N D E V    R L --', width=80, alignment=tcod.constants.CENTER)

        options_x = 3
        options_y = 7
        options_spacing = 2
        cursor_text = Text('-> ')
        for i, option in enumerate(self.options):
            if i == self.cursor:
                cursor_text.print(options_x, options_y+i*options_spacing)
                option.text.print(options_x+len(cursor_text.text), options_y+i*options_spacing)
            else:
                option.text.print(options_x, options_y+i*options_spacing)
