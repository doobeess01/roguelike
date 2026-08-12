from .. import g
from ..state import State


class Game(State):
    def draw(self):
        g.console.print(1,1,'Placeholder Game state')