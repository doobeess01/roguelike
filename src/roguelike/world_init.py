import tcod.ecs

from . import g
from .components import Position, Graphic, Name, HP, Attack
from .tags import IsPlayer, IsActor, BlocksMovement, IsHostile
from .map_init import generate_map
from .simulation import Simulation
from . import callbacks
from .message_log import MessageLog


def initialize_world():
    g.registry = tcod.ecs.Registry()
    callbacks.register_all()

    map_ = generate_map()

    # Add player
    g.player = g.registry.new_entity(
        components={
            Name: 'player',
            Position: Position(5,5, map_),
            Graphic: Graphic(ord('@'),(255,255,255)),
            HP: 10,
            Attack: 2,
        }, 
        tags={IsPlayer, IsActor, BlocksMovement}
    )

    # Add an NPC
    kobold = g.registry.new_entity(
        components={
            Name: 'kobold',
            Position: Position(15,5, map_),
            Graphic: Graphic(ord('K'),(240,120,30)),
            HP: 6,
            Attack: 1,
        }, 
        tags={IsActor, BlocksMovement, IsHostile}
    )

    g.simulation = Simulation()
    g.simulation.add_actor(g.player)
    g.simulation.add_actor(kobold)

    g.message_log = MessageLog()