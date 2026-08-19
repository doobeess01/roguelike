from ..events import Death
from ..entity_tools import get_name


def handle_death(death: Death):
    print(f'The {get_name(death.entity)} dies!')
    death.entity.clear()