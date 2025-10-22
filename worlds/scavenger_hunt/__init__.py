# world/mygame/__init__.py

import settings
import typing
from .options import ScavengerHuntOptions
from .items import all_items
from .locations import all_locations
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, RegionType, ItemClassification

class ScavengerHuntWorld(World):
    """IRL Scavenger Hunt in Archipelago"""
    game = "Scavenger Hunt"
    options_dataclass = ScavengerHuntOptions
    options: ScavengerHuntOptions
    origin_region_name = "Outside"

    item_name_to_id = {name: id for
                       id, name in enumerate(all_items)}
    location_name_to_id = {name: id for
                           id, name in enumerate(all_locations)}