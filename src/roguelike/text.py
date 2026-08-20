from typing import Any
from dataclasses import dataclass

from . import g


@dataclass
class Text:
    text: str
    fg: tuple[int, int, int] = (255, 255, 255)
    bg: tuple[int, int, int] = (0, 0, 0)

    def print(self, x: int, y: int, **kwargs: Any):
        g.console.print(x, y, self.text, fg=self.fg, bg=self.bg, **kwargs)