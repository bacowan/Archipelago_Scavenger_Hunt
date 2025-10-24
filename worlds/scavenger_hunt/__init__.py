import settings
from typing import TYPE_CHECKING
import math
import random
from worlds.scavenger_hunt.constants import LARGE_TRANSIT_FARE_COEFFICIENT, SMALL_TO_LARGE_TRANSIT_FARE_COUNT_RATIO
from .options import ScavengerHuntOptions
from .items import item_classifications, ScavengerHuntItem, filler_items
from .locations import all_locations
from worlds.AutoWorld import World
from BaseClasses import Region

if TYPE_CHECKING:
    from BaseClasses import MultiWorld


class ScavengerHuntWorld(World):
    """IRL Scavenger Hunt in Archipelago"""
    game = "Scavenger Hunt"
    options_dataclass = ScavengerHuntOptions
    options: ScavengerHuntOptions
    origin_region_name = "Outside"

    item_name_to_id = {name: id for
                       id, name in enumerate(item_classifications, 1)}
    location_name_to_id = {name: id for
                       id, name in enumerate(all_locations, 1)}

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        self.large_transit_fare_value = 0
        self.small_transit_fare_value = 0
        self.display_name_to_location_name = {}
        self.location_name_to_display_name = {}

    def create_item(self, item: str) -> ScavengerHuntItem:
        return ScavengerHuntItem(item, item_classifications[item], self.item_name_to_id[item], self.player)

    def get_filler_item_name(self) -> str:
        return random.choice(filler_items)

    def generate_early(self):
        self.display_name_to_location_name = {name: "Check " + str(i) for i, name in enumerate(self.options.checks.value.keys(), 1)}
        self.location_name_to_display_name = {i: name for name, i in self.display_name_to_location_name.items()}

    def create_regions(self) -> None:
        regions = []

        outside = Region("Outside", self.player, self.multiworld)
        outside.add_locations({
            self.display_name_to_location_name.get(item): None
            for item, setting
            in self.options.checks.value.items() if setting.get("found_outdoors") })
        regions.append(outside)

        inside = Region("Inside", self.player, self.multiworld)
        inside.add_locations({
            self.display_name_to_location_name.get(item): None
            for item, setting
            in self.options.checks.value.items() if not setting.get("found_outdoors") })
        regions.append(inside)

        outside.connect(inside)

        self.multiworld.regions.extend(regions)

    def create_items(self) -> None:
        res: list[ScavengerHuntItem] = []

        # Start with the important items
        res.append(self.create_item("Indoor Key"))
        res.append(self.create_item("GPS"))

        # fill the rest with transit fare and filler
        remaining_slots = len(self.options.checks) - len(res)

        # TODO: Error handling if there are not enough slots
        filler_slots = math.ceil(remaining_slots * self.options.filler_ratio / 100)
        transit_fare_slots = remaining_slots - filler_slots

        # start with the transit fare
        total_transit_fare = int(self.options.total_transit_fare.value)
        if transit_fare_slots == 0 and total_transit_fare > 0:
            # If the user configured there to be some money, make sure that there is always at least one
            # check with money
            self.large_transit_fare_value = total_transit_fare
            self.small_transit_fare_value = 0
            res.append(self.create_item("Large Transit Fare"))
        else:
            # create transit fare items to roughly match the requested total transit fare
            self.small_transit_fare_value = round(
                total_transit_fare / transit_fare_slots,
                self.options.currency_granularity.value)
            self.large_transit_fare_value = self.small_transit_fare_value * constants.LARGE_TRANSIT_FARE_COEFFICIENT
            for i in range(transit_fare_slots):
                if i % constants.SMALL_TO_LARGE_TRANSIT_FARE_COUNT_RATIO == 0:
                    res.append(self.create_item("Large Transit Fare"))
                else:
                    res.append(self.create_item("Small Transit Fare"))

        # then filler
        for _ in range(filler_slots):
            res.append(self.create_item(random.choice(filler_items)))

        # add to the world
        self.multiworld.itempool += res