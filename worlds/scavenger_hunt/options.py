from dataclasses import dataclass

from Options import FreeText, Range, PerGameCommonOptions, OptionDict
from worlds.scavenger_hunt.custom_check_schema import custom_check_schema


def isPositiveNumber(val):
    try:
        asNum = float(val)
        return asNum > 0
    except:
        return False

class TotalTransitFare(FreeText):
    # Total amount of money to be spread throughout the world as transit fare items
    display_name = "Total Transit Fare"
    default = 1000

    def __init__(self, value: str):
        if not isPositiveNumber(value):
            raise Exception("Total Transit Fare should be a positive number.")
        super().__init__(self, value)

class CurrencyName(FreeText):
    # Name of the currency
    display_name = "Currency Name"
    default = "yen"
    

class CurrencyGranularity(Range):
    # Number of decimal points to round currency items to. Useful for currencies that have fractional values, like Dollars and cents. 0 will only include whole values. 2 will have 2 decimal places.
    display_name = "Currency Granularity"
    default = 0
    range_start = 0
    range_end = 2

class Checks(OptionDict):
    # A list of all checks that can be done
    display_name = "Checks"
    schema = custom_check_schema
    default = [
        { "name": "Capsule machine purchase", "found_indoors": True, "found_outdoors": True },
        { "name": "Convenience store purchase", "found_indoors": True, "found_outdoors": False },
        { "name": "Decorative Manhole Cover", "found_indoors": False, "found_outdoors": True },
        { "name": "Station Stamp", "found_indoors": True, "found_outdoors": False },
        { "name": "Two of the same store in eyesight", "found_indoors": False, "found_outdoors": True },
    ]



@dataclass
class ScavengerHuntOptions(PerGameCommonOptions):
    total_transit_fare: TotalTransitFare
    currency_name: CurrencyName
    currency_granularity: CurrencyGranularity
    checks: Checks