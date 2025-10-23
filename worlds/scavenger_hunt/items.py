from dataclasses import dataclass
from typing import Literal, get_args
from BaseClasses import Item, ItemClassification

class ScavengerHuntItem(Item):
    game = "Scavenger Hunt"

class ScavengerHuntMoneyItem(ScavengerHuntItem):
    amount: int

item_classifications: dict[str, ItemClassification] = {
    "Small Transit Fare": ItemClassification.progression_skip_balancing,
    "Large Transit Fare": ItemClassification.progression_skip_balancing,
    "Indoor Key": ItemClassification.progression,
    "GPS": ItemClassification.progression
}

all_items = item_classifications.keys()