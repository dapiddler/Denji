#!/usr/bin/env python
import maestro
import time
from network import get_ip
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
servo = maestro.Controller()

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
api.add_resource(HelloWorld, '/')

class Step(Resource):
    def get(self):
        servo.runScriptSub(2)
        print("step")
        return {'postion': 'forward step'}
api.add_resource(Step, '/step')

class Crouch(Resource):
    def get(self):
        servo.runScriptSub(0)
        print("crouch")
        return {'postion': 'crouch'}
api.add_resource(Crouch, '/crouch')


class Taunt(Resource):
    def get(self):
        servo.runScriptSub(1)
        print("taunt")
        return {'postion': 'taunt'}
api.add_resource(Taunt, '/taunt')


class Neutral(Resource):
    def get(self):
        servo.runScriptSub(1)
        print("neutral")
        return {'postion': 'neutral'}
api.add_resource(Neutral, '/neutral')


if __name__ == '__main__':
    rpiIP = str(get_ip())  # sets ip address of raspberry pi
    app.run(debug=True, host=str(rpiIP))


