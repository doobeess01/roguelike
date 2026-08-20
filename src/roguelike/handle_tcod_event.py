from tcod.event import Event, Quit, KeyDown

from . import g
from .keybindings import get_keybindings


def handle_tcod_event(event: Event):
    state = g.state_manager.state

    match event:
        case Quit():
            raise SystemExit
        case KeyDown(sym=sym):
            keybindings = get_keybindings(state)
            if (key_name := sym.label.lower()) in keybindings:
                action_str = keybindings[key_name]
                state.execute_action(action_str)
        case _:
            pass