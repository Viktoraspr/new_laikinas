"""
github mr
dataclass -> dict

"""
from dataclasses import dataclass


@dataclass
class FuelPrice:
    petrol: float = 1.51
    diesel: float = 1.55


data = {
    'petrol': 1.51,
    'diesel': 1.55,
}
