from .. import g
from ..events import Damage, Death
from ..components import HP
from ..entity_tools import get_name


def apply_damage(damage: Damage):
    damage.target.components[HP] -= damage.amount
    print(f"{get_name(damage.source)} attacks {get_name(damage.target)} for {damage.amount} damage!")

    if damage.target.components[HP] <= 0:
        g.event_bus.emit(Death(entity=damage.target))