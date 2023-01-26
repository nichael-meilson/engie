'''
Michael Neilson <github: nichael-meilson>
2023-01-25
'''

from fastapi import FastAPI

import src.api as api

app = FastAPI()
app.include_router(api.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
