'''
Michael Neilson <github: nichael-meilson>
2023-01-25
'''
from fastapi import APIRouter

from src.api.productionplan.post import post_productionplan_endpoint

router = APIRouter(prefix="/productionplan")
post_productionplan_endpoint(router)