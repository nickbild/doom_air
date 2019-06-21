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

class Forward(Resource):
    def get(self):
        autopy.key.toggle(autopy.key.Code.UP_ARROW, True, [], 0)
        time.sleep(key_hold_time_sec)
        autopy.key.toggle(autopy.key.Code.UP_ARROW, False, [], 0)
        return None

class Backward(Resource):
    def get(self):
        autopy.key.toggle(autopy.key.Code.DOWN_ARROW, True, [], 0)
        time.sleep(key_hold_time_sec)
        autopy.key.toggle(autopy.key.Code.DOWN_ARROW, False, [], 0)
        return None

class Left(Resource):
    def get(self):
        autopy.key.toggle(autopy.key.Code.LEFT_ARROW, True, [], 0)
        time.sleep(key_hold_time_sec)
        autopy.key.toggle(autopy.key.Code.LEFT_ARROW, False, [], 0)
        return None

class Right(Resource):
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

class Fire(Resource):
    def get(self):
        autopy.key.tap("a", [])
        return None

class Jump(Resource):
    def get(self):
        autopy.key.tap("q", [])
        return None

class Crouch(Resource):
    def get(self):
        autopy.key.tap("z", [])
        return None

class NextWeapon(Resource):
    def get(self):
        autopy.key.tap("p", [])
        return None

class PreviousWeapon(Resource):
    def get(self):
        autopy.key.tap("o", [])
        return None

class GodMode(Resource):
    def get(self):
        autopy.key.type_string("iddqd", wpm=60)
        return None

class AllItems(Resource):
    def get(self):
        autopy.key.type_string("idkfa", wpm=60)
        return None


###
# Attach endpoints.
###

api.add_resource(Forward, '/forward')
api.add_resource(Backward, '/backward')
api.add_resource(Left, '/left')
api.add_resource(Right, '/right')

api.add_resource(Fire, '/fire')
api.add_resource(Jump, '/jump')
api.add_resource(Crouch, '/crouch')
api.add_resource(NextWeapon, '/next_weapon')
api.add_resource(PreviousWeapon, '/previous_weapon')

api.add_resource(Control, '/control')
api.add_resource(Space, '/space')

api.add_resource(GodMode, '/god_mode')
api.add_resource(AllItems, '/all_items')


###
# Start server.
###

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
