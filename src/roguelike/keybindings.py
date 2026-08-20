from tcod.event import KeySym as K

from .state import State
from .states import Game, Menu

def get_keybindings(state: State) -> dict[str, str]:
    keybindings_sets = (KEYBINDINGS[state_type] for state_type in type(state).__mro__ if state_type in KEYBINDINGS)
    keybindings: dict[str, str] = {}
    for keybindings_set in keybindings_sets:
        keybindings |= keybindings_set
    return keybindings
    
def name(sym: K):
    return sym.label.lower()


DIRECTIONS_TO_KEYSYMS: dict[str, list[K]] = {
    'north': [K.UP, K.N8, K.KP_8],
    'northeast': [K.N9, K.KP_9],
    'east': [K.RIGHT, K.N6, K.KP_6],
    'southeast': [K.N3, K.KP_3],
    'south': [K.DOWN, K.N2, K.KP_2],
    'southwest': [K.N1, K.KP_1],
    'west': [K.LEFT, K.N4, K.KP_4],
    'northwest': [K.N7, K.KP_7]
}
KEYNAMES_TO_DIRECTIONS: dict[str, str] = {}
for direction, syms in DIRECTIONS_TO_KEYSYMS.items():
    for sym in syms:
        KEYNAMES_TO_DIRECTIONS[name(sym)] = direction



KEYBINDINGS: dict[type[State], dict[str, str]] = {}


KEYBINDINGS[Menu] = {
    name(K.UP): Menu.CURSOR_UP,
    name(K.DOWN): Menu.CURSOR_DOWN,
    name(K.RETURN): Menu.SELECT,
}


KEYBINDINGS[Game] = {
    name(K.PERIOD): Game.WAIT,
}
# Add movement keybindings
KEYBINDINGS[Game] |= {sym: Game.MOVE(direction) for sym, direction in KEYNAMES_TO_DIRECTIONS.items()}