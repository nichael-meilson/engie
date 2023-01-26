'''
Michael Neilson <github: nichael-meilson>
2023-01-25
'''
from src.entities.data import Data


class ProductionPlan(Data):
    load: int
    fuels: dict
    powerplants: list
