from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api


app = Flask("Devices")
app.config.from_object('config.Config')

api = Api(app)
jwt = JWTManager(app)
















