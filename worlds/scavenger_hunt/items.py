from dataclasses import dataclass
from typing import Literal, get_args
from BaseClasses import Item, ItemClassification

class ScavengerHuntItem(Item):
    game = "Scavenger Hunt"

class ScavengerHuntMoneyItem(ScavengerHuntItem):
    amount: int

AllItems = Literal[
    "Transit Fare",
    "Indoor Key",
    "GPS"
]

all_items = get_args(AllItems)