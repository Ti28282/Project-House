from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, decode_token
from flask import jsonify, request
import uuid
from json import dumps
from schema import DeviceSchema
from redis_client import redis_client
class Provited(Resource):

    @jwt_required()
    def get(self):
        user = get_jwt_identity()
        return jsonify(Message = f"User {user} has access")
        
# TEST CONNECT 
# User enter to Account
# Next js Generation url
# device witch want to connect go in url send access_token and device append to Account


class DeviceConnect(Resource):

    @jwt_required()
    def post(self):

        token = request.args.get("token")
        if not token: return jsonify(Error = "Missing token")

        try:
            decoded = decode_token(token)
            user_id = decoded["sub"]
            device_id = str(uuid.uuid4())

            data = request.get_json()
            
            valid_data = DeviceSchema(
                device_id = device_id,
                user_id = user_id,
                **data    
            )
            
            if not valid_data.device_name or not valid_data.device_type or not valid_data.ip:
                return jsonify(Error = "not device_name or device_type, ip")
            
            
            device_key = f"device:{device_id}"
            device_data = {
                "device_id": valid_data.device_id,
                "user_id": user_id,
                "device_name": valid_data.device_name,
                "device_type": valid_data.device_type,
                "ip": valid_data.ip,
                "online": True

            }
            

            #todo Save Data to Redis
            redis_client.setex(device_key, 3600, dumps(device_data))
            
            redis_client.sadd(f"user_device:{user_id}", device_id)

            return jsonify(message = "You are connect", device_id = device_id)

        except Exception as e:
            return jsonify(Error = f"Invalid token: {str(e)}")
                