'''
Michael Neilson <github: nichael-meilson>
2023-01-25
'''
from typing import Any

import fastapi
import pydantic

from src.entities.productionplan import ProductionPlan
from src.models.productionplan import ProductionPlanModel
from src.usecases.post_a_productionplan import post_a_productionplan, CreateProductionPlanInput, \
    CreateProductionPlanOutput


class ProductionPlanRequest(pydantic.BaseModel):
    load: int = pydantic.Field(..., description="load")
    fuels: dict = pydantic.Field(..., description="fuels")
    powerplants: list = pydantic.Field(..., description="load")

    def to_entity(self) -> ProductionPlan:
        return ProductionPlan(
            load=self.load,
            fuels=self.fuels,
            powerplants=self.powerplants
        )


class ProductionPlanResponse(pydantic.BaseModel):
    responses: ProductionPlanModel = pydantic.Field(..., description="response model")


class Input(CreateProductionPlanInput):
    __slots__ = "__body"

    def __init__(self, body: ProductionPlanRequest):
        self.__body = body

    async def get_productionplan_data(self) -> ProductionPlan:
        return self.__body.to_entity()


class Output(CreateProductionPlanOutput):
    __slots__ = "response"

    def __init__(self):
        self.response: Any = None

    # async def success(self, plan: ProductionPlan):
    #     self.response = ProductionPlanResponse(
    #         responses=ProductionPlanModel.from_entity(plan)
    #     )


def post_productionplan_endpoint(router: fastapi.APIRouter, path: str = ""):
    @router.post(path, response_model=ProductionPlanResponse)
    async def endpoint(
            body: ProductionPlanRequest = fastapi.Body(..., description="Request body ingested")
    ):
        input_ = Input(body)
        output = Output()
        await post_a_productionplan(input_, output)
        return output.response