# world/mygame/__init__.py

import settings
import typing
from .options import ScavengerHuntOptions
from .items import mygame_items
from .locations import mygame_locations
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, RegionType, ItemClassification

class ScavengerHuntWorld(World):
    """IRL Scavenger Hunt in Archipelago"""
    game = "Scavenger Hunt"
    options_dataclass = ScavengerHuntOptions
    options: ScavengerHuntOptions

    item_name_to_id = {name: id for
                       id, name in enumerate(mygame_items, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(mygame_locations, base_id)}

    item_name_groups = {
        "weapons": {"sword", "lance"},
    }

    item_name_to_id = {name: id for
                       id, name in enumerate(mygame_items, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(mygame_locations, base_id)}