from collector import app, api
from routes import Provited, DeviceConnect


api.add_resource(Provited, "/device/v1/protected")
api.add_resource(DeviceConnect, "/device/v1/connect")



if __name__ == "__main__":
    app.run(port = 5002, debug = True)
