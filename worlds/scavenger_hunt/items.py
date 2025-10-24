from dataclasses import dataclass
from typing import Literal, get_args, TYPE_CHECKING
from BaseClasses import Item, ItemClassification

class ScavengerHuntItem(Item):
    game = "Scavenger Hunt"

progression_items = [
    "Indoor Key",
    "GPS"
]

money_items = [
    "Small Transit Fare",
    "Large Transit Fare"
]

filler_items = [
    "Change App Theme",
    "Fireworks",
    "Joke"
]

item_classifications = {
    **{ name: ItemClassification.progression for name in progression_items },
    **{ name: ItemClassification.progression_skip_balancing for name in money_items },
    **{ name: ItemClassification.filler for name in filler_items }
}