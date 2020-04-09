import os
import sys
import redis

from argparse import ArgumentParser

from flask import Flask, request, abort, send_file, render_template


import pandas as pd
from module.resource import *
from module.map import *

app = Flask(__name__, static_folder='web-robot-frontend')

# # get channel_secret and channel_access_token from your environment variable
# channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)

# obtain the port that heroku assigned to this app.
heroku_port = os.getenv('PORT', 9001)

# if channel_secret is None:
#     print('Specify LINE_CHANNEL_SECRET as environment variable.')
#     sys.exit(1)


# test
@app.route("/hello/", methods=['GET'])
def hello():
    return 'hello world!'

@app.route("/map/", methods=['GET'])
def map():
    return send_file(getMap())

@app.route("/resource/", methods=['GET'])
def pathResource():
    resource = getResource()
    print(resource)
    return render_template('resource.html', resource=resource)

@app.route("/resource", methods=['POST'])
def pathResourceLoad():
    loadDataToRedis()
    return 'ok'

@app.route("/map", methods=['POST'])
def pathMapLoad():
    loadMapToRedis()
    return 'ok'

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(host='0.0.0.0', debug=options.debug, port=heroku_port)
