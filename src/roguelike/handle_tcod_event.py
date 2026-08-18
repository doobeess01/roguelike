from tcod.event import Event, Quit, KeyDown

from . import g
from .keybindings import KEYBINDINGS


def handle_tcod_event(event: Event):
    match event:
        case Quit():
            raise SystemExit
        case KeyDown(sym=sym) if type(g.state_manager.state) in KEYBINDINGS:
            keybindings = KEYBINDINGS[type(g.state_manager.state)]
            if (key_name := sym.label.lower()) in keybindings:
                action_str = keybindings[key_name]
                g.state_manager.state.execute_action(action_str)
        case _:
            pass