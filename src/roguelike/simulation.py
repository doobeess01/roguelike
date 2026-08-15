from . import g
from .tags import IsActor
from .ai import ai_choose_action
from .entity_tools import get_name


def handle_npc_turns():
    for actor in g.registry.Q.all_of(tags=[IsActor]):
        if actor == g.player:
            continue
        action = ai_choose_action(actor)
        feedback = action(actor)  # Execute the action
        if feedback is not None:  # Print a warning if the NPC action failed (to attempt) -- this should only happen with player actions
            print(f'WARNING: {get_name(actor)} failed to attempt the selected action!')