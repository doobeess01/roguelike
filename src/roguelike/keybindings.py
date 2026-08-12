from tcod.event import KeySym as K

from .state import State
from . import states


def name(sym: K):
    return sym.label.lower()


KEYBINDINGS: dict[type[State], dict[str, str]] = {
    states.MainMenu: {
        name(K.RETURN): states.MainMenu.BEGIN,
    }
}