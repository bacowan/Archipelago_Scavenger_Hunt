from typing import Literal
from BaseClasses import Location

class ScavengerHuntLocation(Location):
    game = "Scavenger Hunt"



all_locations = Literal[
    "Capsule Machine Purchase",
    "Convenience Store Snack Purchase",
    "Decorated Manhole"
]