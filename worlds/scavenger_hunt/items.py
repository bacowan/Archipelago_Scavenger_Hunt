from dataclasses import dataclass
from typing import Literal
from BaseClasses import Item, ItemClassification

class ScavengerHuntItem(Item):
    game = "Scavenger Hunt"

class ScavengerHuntMoneyItem(ScavengerHuntItem):
    amount: int

all_items = Literal[
    "Transit Fare",
    "Indoor Key"
]