from ..events import Death
from ..entity_tools import get_name


def report_death(death: Death):
    print(f'The {get_name(death.entity)} dies!')
    

def clear_dead_entity(death: Death):
    death.entity.clear()