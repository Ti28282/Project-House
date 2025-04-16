from os import environ
from dotenv import load_dotenv


load_dotenv()

class Config:

    SECRET_KEY = environ.get('DEVICE_SECRET_KEY')

    JWT_SECRET_KEY  = environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = ("json", "headers")
    JWT_COOKIE_SECURE = False
    REDIS_URL = environ.get("REDIS_URL", "redis://localhost:6379/0")

