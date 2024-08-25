import requests
from fastapi import FastAPI

from tracing import init_tracing
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor



app = FastAPI()

init_tracing()
FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()
# Additional instrumentation can be enabled by
# following the docs for respective instrumentations at
# https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation


@app.get("/")
async def home():
    return {"Hello": "World"}


@app.get("/param/{param}")
async def param(param: str):
    return {"param": param}


@app.get("/exception")
async def exception():
    raise Exception("Sample exception")


@app.get("/api")
async def api():
    requests.get('http://localhost:8000/')
    return {"api": "called"}
