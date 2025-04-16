from collector import app, api
from routes import SignIn, SignUp, RefreshToken


api.add_resource(SignIn, "/auth/v1/signin")
api.add_resource(SignUp, "/auth/v1/signup")
api.add_resource(RefreshToken, "/auth/v1/refresh")



if __name__ == "__main__":
    
    app.run(port = 5001, debug = True)
    
    




