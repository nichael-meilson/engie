'''
Michael Neilson <github: nichael-meilson>
2023-01-25
'''
import abc
import pandas as pd

from src.entities.productionplan import ProductionPlan


class CreateProductionPlanInput(abc.ABC):
    __slots__ = "__body"

    async def get_productionplan_data(self) -> ProductionPlan:
        """Get production plan data"""


class CreateProductionPlanOutput(abc.ABC):
    __slots__ = "response"


async def post_a_productionplan(input_: CreateProductionPlanInput, output: CreateProductionPlanOutput):
    data = await input_.get_productionplan_data()

    # Powerplant dataframe
    pp_df = pd.DataFrame(data.powerplants)
    print(pp_df)
    print("******")
    # ordered_pp_df = pp_df.sort_values(by=['efficiency'], ascending=False)

    # Wind turbines
    wt = pp_df[pp_df['type'] == "windturbine"]
    wt["output"] = wt["pmax"]*(data.fuels["wind(%)"]/100)
    print(wt)

    # Gas fired
    gf = pp_df[pp_df["type"] == "gasfired"]
    print(gf)
    # Continue with logic to determine gas fired plants output based on cost and efficiency

    # Jet powered
    # Similar logic as above

    # Union dataframes

    # Loop over "output" column and subtract from "load" until it reaches 0

    # Format results and assign to the output.response variable





