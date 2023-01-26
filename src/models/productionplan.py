'''
Michael Neilson <github: nichael-meilson>
2023-01-25
'''

import pydantic


class ProductionPlanModel(pydantic.BaseModel):
    name: str
    p: int
