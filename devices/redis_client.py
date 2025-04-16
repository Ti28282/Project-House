from redis import StrictRedis
from os import environ
from dotenv import load_dotenv

from config import Config

load_dotenv()

redis_client = StrictRedis.from_url(
    Config.REDIS_URL, 
    decode_responses = True,
    password = environ.get("REDIS_PASSWORD")
    )



