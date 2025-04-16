from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask_talisman import Talisman


from flask_caching import Cache

app = Flask("auth")
app.config.from_object('config.Config')

# ! Flask-CORS
CORS(app)

# ! Flask-Talisman
Talisman(app, content_security_policy = None)


#! Limiter 
limiter = Limiter(
    key_func = get_remote_address, 
    storage_uri="memory://"
    )

limiter.init_app(app)



bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
