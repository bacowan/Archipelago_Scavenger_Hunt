from typing import Literal, get_args
from BaseClasses import Location

class ScavengerHuntLocation(Location):
    game = "Scavenger Hunt"



AllLocations = Literal[
    "Custom Location"
]
all_locations = get_args(AllLocations)