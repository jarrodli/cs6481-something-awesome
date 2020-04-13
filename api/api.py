from flask import Flask, request
import backend as be
from flask_cors import CORS
import json

APP = Flask(__name__)
CORS(APP)

@APP.route("/")
def init():
    return "hello"

@APP.route("/readdb", methods = ['GET'])
def readdb():
    return json.dumps(be.read_database())

@APP.route("/writedb", methods = ["PUT"])
def writedb():
    data = request.get_json(force=True)
    return json.dumps(be.write_database(data))

@APP.route("/dropdb", methods = ["DELETE"])
def dropdb():
    return json.dumps(be.drop_column())

if __name__ == "__main__":
    APP.run(debug=True, host="0.0.0.0", port=4000)
