from typing import Literal, get_args
from BaseClasses import Location
from worlds.scavenger_hunt.constants import MAX_CHECKS


class ScavengerHuntLocation(Location):
    game = "Scavenger Hunt"

# checks need to be known at compile time, so a bunch are generated right off the bat with numbered names
all_locations = ["Check " + str(n) for n in range(1, MAX_CHECKS)]

def assign_ids(location_names: list[str]) -> dict[str, int]:
    return {name: i for i, name in enumerate(location_names, 1)}