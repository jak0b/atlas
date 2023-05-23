from flask import Flask, Response
import redis
import os

app = Flask(__name__)

# redis database
REDIS_URL = os.getenv('REDIS_URL')
db = redis.Redis.from_url(REDIS_URL)

from app import routes




