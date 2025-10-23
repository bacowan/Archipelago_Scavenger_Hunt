from typing import TYPE_CHECKING
from BaseClasses import Region

if TYPE_CHECKING:
    from . import ScavengerHuntWorld

def create_regions(world: ScavengerHuntWorld):
    regions = [
        Region("Outside", world.player, world.multiworld),
        Region("Inside", world.player, world.multiworld)
    ]
    return regions