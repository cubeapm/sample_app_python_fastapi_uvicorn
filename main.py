import requests
import mysql.connector
import redis
from fastapi import FastAPI

app = FastAPI()

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