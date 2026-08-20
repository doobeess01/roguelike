from .. import g
from ..events import Death
from ..entity_tools import get_name
from .. import colors


def report_death(death: Death):
    g.message_log.log(f'The {get_name(death.entity)} dies!', *colors.messages.ENTITY_DIED)
    

def clear_dead_entity(death: Death):
    death.entity.clear()
    g.simulation.remove_actor(death.entity)