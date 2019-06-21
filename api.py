########
# Nick Bild
# nick.bild@gmail.com
#
# Doom AIr
#
# This is a REST API server that will simulate keystrokes on the host machine
# when API endpoints are requested.  It allows a remote machine to effectively
# press buttons on the server's keyboard and control any arbitrary application.
# Yes, that is a security risk.  A big huge one.  This should only be used
# on a firewalled machine by those that understand the risks.
#
# Required libraries:
#   flask
#   flask-restful
#   autopy
#
# Developed on Python 3.7.0.
#
# Starting the server:
# python3 api.py
#
# Accessing an endpoint:
# curl http://[SERVER_IP]:5000/[ENDPOINT_NAME]
########

from flask import Flask
from flask_restful import Resource, Api
import autopy
import time


key_hold_time_sec = 0.1

app = Flask(__name__)
api = Api(app)


###
# Define endpoint actions.
###

class UpArrow(Resource):
    def get(self):
        autopy.key.toggle(autopy.key.Code.UP_ARROW, True, [], 0)
        time.sleep(key_hold_time_sec)
        autopy.key.toggle(autopy.key.Code.UP_ARROW, False, [], 0)
        return None

class DownArrow(Resource):
    def get(self):
        autopy.key.toggle(autopy.key.Code.DOWN_ARROW, True, [], 0)
        time.sleep(key_hold_time_sec)
        autopy.key.toggle(autopy.key.Code.DOWN_ARROW, False, [], 0)
        return None

class LeftArrow(Resource):
    def get(self):
        autopy.key.toggle(autopy.key.Code.LEFT_ARROW, True, [], 0)
        time.sleep(key_hold_time_sec)
        autopy.key.toggle(autopy.key.Code.LEFT_ARROW, False, [], 0)
        return None

class RightArrow(Resource):
    def get(self):
        autopy.key.toggle(autopy.key.Code.RIGHT_ARROW, True, [], 0)
        time.sleep(key_hold_time_sec)
        autopy.key.toggle(autopy.key.Code.RIGHT_ARROW, False, [], 0)
        return None

class Control(Resource):
    def get(self):
        autopy.key.tap(autopy.key.Code.CONTROL, [])
        return None

class Space(Resource):
    def get(self):
        autopy.key.tap(autopy.key.Code.SPACE, [])
        return None


###
# Attach endpoints.
###

api.add_resource(UpArrow, '/up')
api.add_resource(DownArrow, '/down')
api.add_resource(LeftArrow, '/left')
api.add_resource(RightArrow, '/right')

api.add_resource(Control, '/control')
api.add_resource(Space, '/space')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
