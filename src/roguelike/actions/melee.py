from tcod.ecs import Entity

from .. import g
from ..action import Impossible
from .directional import Directional
from ..components import Position, Attack
from ..tags import IsFighter
from ..events import Damage


class Melee(Directional):
    class NoFighterThere(Impossible):
        def report(self):
            print('No fighter there.')

    def check(self, actor: Entity) -> Impossible | None:
        dest = actor.components[Position] + self.direction
        if entities := g.registry.Q.all_of(tags=[dest, IsFighter]):
            # There should only ever be one fighter entity per square
            assert len(list(entities)) == 1
        else:
            return Melee.NoFighterThere()

    def _execute(self, actor: Entity):
        dest = actor.components[Position] + self.direction
        target = list(g.registry.Q.all_of(tags=[dest, IsFighter]))[0]
        damage_amount = actor.components[Attack]
        g.event_bus.emit(Damage(source=actor, target=target, amount=damage_amount))
