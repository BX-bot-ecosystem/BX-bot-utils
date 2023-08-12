import redis
from dotenv import load_dotenv
import os

load_dotenv()
_REDIS_HOST = os.getenv("REDIS_HOST")
_REDIS_PORT = int(os.getenv("REDIS_PORT"))

r = redis.Redis(host=_REDIS_HOST, port=_REDIS_PORT, decode_responses=True)
