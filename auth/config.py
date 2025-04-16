from os import environ
from dotenv import load_dotenv
import datetime

load_dotenv()

class Config:
    """Base config"""
    SECRET_KEY = environ.get('SECRET_KEY')

    # * Sqlalchemy
    # todo Postgres config for connect
    user_db = environ.get('USER_DB')
    password_db = environ.get('PASSWORD_DB')
    host_db = environ.get('HOST_DB')
    port_db = environ.get('PORT_DB')
    name_db = environ.get('NAME_DB')
    
    SQLALCHEMY_DATABASE_URI = f"postgresql://{user_db}:{password_db}@{host_db}:{port_db}/{name_db}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # todo JWT 
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = ("headers","cookies","query_string")
    JWT_COOKIE_SECURE = False #! If https -> True
    JWT_COOKIE_CSRF_PROTECT = False #! While False
    # todo TIME 
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours = 1)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days = 5)

class ProductionConfig(Config):
    """Production config."""
    FLASK_ENV = "production"
    FLASK_DEBUG = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')

class DevConfig(Config):
    """Development config."""
    FLASK_ENV = "development"
    FLASK_DEBUG = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')


