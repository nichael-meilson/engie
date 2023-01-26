'''
Michael Neilson <github: nichael-meilson>
2023-01-25
'''
from fastapi import APIRouter

from src.api import productionplan

router = APIRouter(prefix="/api")
router.include_router(productionplan.router)
