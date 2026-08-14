from . import g
from .tags import IsActor
from .ai import ai_choose_action
from .action import Success


def handle_npc_turns():
    for actor in g.registry.Q.all_of(tags=[IsActor]):
        if actor == g.player:
            continue
        action = ai_choose_action(actor)
        feedback = action(actor)  # Execute the action
        assert isinstance(feedback, Success)  # Make sure that the NPC action didn't fail -- this should only happen with player actions