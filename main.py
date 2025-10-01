import requests
import mysql.connector
import redis
# import logging
from fastapi import FastAPI
from elasticapm.contrib.starlette import ElasticAPM

app = FastAPI()
app.add_middleware(ElasticAPM)

# If using ELASTIC_APM_LOG_LEVEL to check agent debug logs, 
# The following may need to be uncommented to see the logs.

# logging.basicConfig()

cnx = mysql.connector.connect(
    user='root', password='root', host='mysql', database='test')

redis_conn = redis.Redis(host='redis', port=6379, decode_responses=True)


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


@app.get("/mysql")
def get_user():
    cursor = cnx.cursor()
    cursor.execute("SELECT NOW()")
    row = cursor.fetchone()
    return str(row)


@app.get("/redis")
async def redis():
    redis_conn.set('foo', 'bar')
    return {"Redis": "Redis called"}