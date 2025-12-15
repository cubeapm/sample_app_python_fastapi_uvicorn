import requests
import mysql.connector
import redis
from fastapi import FastAPI
import logging
from logging_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI()

cnx = mysql.connector.connect(
    user='root', password='root', host='mysql', database='test')

redis_conn = redis.Redis(host='redis', port=6379, decode_responses=True)


@app.get("/")
async def home():
    logger.info("Home endpoint called")
    return {"Hello": "World"}


@app.get("/param/{param}")
async def param(param: str):
    logger.info("param function called")
    return {"param": param}


@app.get("/exception")
async def exception():
    logger.info("exception function called")
    raise Exception("Sample exception")


@app.get("/api")
async def api():
    logger.info("api function called")
    requests.get('http://localhost:8000/')
    return {"api": "called"}


@app.get("/mysql")
def get_user():
    logger.info("mysql function called")
    cursor = cnx.cursor()
    cursor.execute("SELECT NOW()")
    row = cursor.fetchone()
    return str(row)


@app.get("/redis")
async def redis():
    logger.info("redis function called")
    redis_conn.set('foo', 'bar')
    return {"Redis": "Redis called"}