from flask_restful import Resource
from flask import Response, request, jsonify
from collector import db
from werkzeug.exceptions import BadRequest


from models import Users

from sqlalchemy import exc
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, set_refresh_cookies

from pydantic import ValidationError
from schema import UserSchema



#todo change return RESPONSE TEXT

# ! Test For <SignIn, SignUp> написать тесты and if
# ! Refresh saved in cookies check test
# ! Logout delete token refresh from cookies
# ! Поставить ограничение запросов
# ! Connect Redis(Docker)


# todo SignIn make and test all Resources


class SignIn(Resource):
    def post(self):
        try:
            #todo validation JSON form
            valid_data = UserSchema(**request.get_json())
            
            
            if valid_data:
                user = Users.query.filter_by(login = valid_data.login).first()

                if user:
                    if Users.check_password(user, valid_data.password):
                        access_token = create_access_token(identity = str(user.id))
                        refresh_token = create_refresh_token(identity = str(user.id))

                        response = jsonify(access_token = access_token)
                        #todo Set refresh token in Cookies
                        set_refresh_cookies(response,refresh_token)

                        return response

                    return jsonify(ERROR = "Error Password")

                return jsonify(WARNING = "User not found")

            return jsonify(ERROR = "ValidationError :- the json form")
        
        except ValidationError as e:
            return jsonify(ERROR = f"ValidationError :- Invalid JSON format {e}")
        
        except Exception as e:
            return jsonify(ERROR = f"Internal Server Error :- {e}")

class SignUp(Resource):

    def post(self) -> Response:
        try:
            valid_data = UserSchema(**request.get_json())
            
            if valid_data:
                    
                    # * if User doesn't exists add 
                    try:

                        check_user = Users.query.filter_by(login = valid_data.login).first()
                        if not check_user:
                            user = Users(login = valid_data.login, password = valid_data.password)
                            db.session.add(user)
                            db.session.commit()

                            return jsonify(INFO = f"User {valid_data.login} added")

                        return jsonify(INFO = f"User {valid_data.login} already exists")

                    except exc.OperationalError as e:
                        return jsonify(OperationalError = e)
                

            return jsonify(ValidationError = "Error in the json form")

        except Exception as e:
            return jsonify(ExceptionError = e)

class RefreshToken(Resource):
    
    @jwt_required(refresh=True)
    def post(self):
        user_id = get_jwt_identity()
        new_access_token = create_access_token(identity = user_id)
        
        return jsonify(access_token = new_access_token)

class Logout(Resource):
    pass