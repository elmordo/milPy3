import enum
from typing import Union


class CalculationType(enum.Enum):
    FORECAST = "forecast"
    SAFETYSTOCK = "safetystock"
    DELIVERIES = "deliveries"


"""
extendovani neni povoleno!

class ExtendedCalculationType(CalculationType):
    NONE = "none"
"""


class ExtendedCalculationType(enum.Enum):
    NONE = "none"


def calculate_standard(calc_type: CalculationType):
    pass


def calculate_extended(calc_type: Union[CalculationType, ExtendedCalculationType]):
    pass


to_calculate = CalculationType.FORECAST

print(to_calculate.name)
print(to_calculate.value)

print("Is forecast?", to_calculate is CalculationType.FORECAST)
print("Is safetystock?", to_calculate is CalculationType.SAFETYSTOCK)
print("Is type of CalculationType?", isinstance(to_calculate, CalculationType))
