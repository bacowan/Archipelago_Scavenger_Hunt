from dataclasses import dataclass

from Options import FreeText, Range, PerGameCommonOptions

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


@dataclass
class ScavengerHuntOptions(PerGameCommonOptions):
    total_transit_fare: TotalTransitFare
    currency_name: CurrencyName
    currency_granularity: CurrencyGranularity