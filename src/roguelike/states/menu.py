from collections.abc import Iterable, Callable
from dataclasses import dataclass
from ..state import State
from ..text import Text


type OnSelect = Callable[[], None]


@dataclass
class MenuOption:
    text: Text
    on_select: OnSelect


class Menu(State):
    CURSOR_UP = 'cursor_up'
    CURSOR_DOWN = 'cursor_down'
    SELECT = 'select'

    def __init__(self, options: Iterable[MenuOption]) -> None:
        self.actions = {
            Menu.CURSOR_UP: self.move_cursor_up,
            Menu.CURSOR_DOWN: self.move_cursor_down,
            Menu.SELECT: self.select,
        }
        self.options: list[MenuOption] = list(options)
        self.cursor = 0

    def move_cursor_up(self):
        self.cursor -= 1
        if self.cursor < 0:
            self.cursor = len(self.options) - 1

    def move_cursor_down(self):
        self.cursor += 1
        if self.cursor > len(self.options) - 1:
            self.cursor = 0

    def select(self):
        self.options[self.cursor].on_select()

    def get_texts(self):
        return [option.text for option in self.options]