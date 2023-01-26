1. Interpreter used: Python 3.10
2. Terminal: `pip install -r requirements.txt`
3. Terminal: `uvicorn src.api.server:app --reload --port=8888`
4. Browser URL: `127.0.0.1:8888/docs`
5. Expand `[POST] /api/productionplan` endpoint --> Click `Try it out`
6. Copy the (example payload json)[https://github.com/gem-spaas/powerplant-coding-challenge/blob/master/example_payloads/payload1.json] and paste into the request body
7. Click `Execute`