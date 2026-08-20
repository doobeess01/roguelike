from .. import g
from ..events import Damage, Death
from ..components import HP
from ..entity_tools import get_name
from .. import colors


def apply_damage(damage: Damage):
    damage.target.components[HP] -= damage.amount

    message_color = (colors.messages.PLAYER_ATTACKS_NPC if damage.source == g.player else colors.messages.NPC_ATTACKS_PLAYER) if g.player in (damage.source, damage.target) else colors.messages.NPC_ATTACKS_NPC
    g.message_log.log(f"{get_name(damage.source)} attacks {get_name(damage.target)} for {damage.amount} damage!", *message_color)

    if damage.target.components[HP] <= 0:
        g.event_bus.emit(Death(entity=damage.target))