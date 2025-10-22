from typing import TYPE_CHECKING
from BaseClasses import Region

if TYPE_CHECKING:
    from . import ScavengerHuntWorld

def create_regions(world: ScavengerHuntWorld):
    regions = []
    regions.append(Region("Outside", world.player, world.multiworld))
    regions.append(Region("Inside", world.player, world.multiworld))
    return regions