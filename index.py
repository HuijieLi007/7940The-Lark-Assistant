import os
import sys
import redis

from argparse import ArgumentParser

from flask import Flask, request, abort, send_file

from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd


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
    # adjust the province_data
    df = pd.read_csv('province-number.csv')
    data_pair = []
    for index, row in df.iterrows():
        data_pair.append([row['province_cn'], row['number']])

    # adjust the color range based on the confirmed case
    range_color = []
    i = 0
    while i <= 54406:
        if i <= 10:
            range_color.append('#f2dadb')
        if i > 10 and i <= 99:
            range_color.append('#ce8a86')
        if i > 99 and i <= 980:
            range_color.append('#bf5a53')
        if i > 980 and i <= 9999:
            range_color.append('#9e0707')
        if i > 9999 and i <= 54406:
            range_color.append('#600a0a')
        i = i + 1


    map = (
        Map(
            init_opts=opts.InitOpts(
                                width='100%',
                                height='600px'
                            )
        )
        .add(
            zoom=1.1,
            is_roam=False, 
            maptype="china", 
            data_pair=data_pair, 
            series_name="confirmed case", 
        )
        .set_global_opts(
            visualmap_opts = opts.VisualMapOpts(
                                                min_=1,
                                                max_=55000, 
                                                is_show = False,
                                                pos_left = 'left', 
                                                range_color=range_color
                                           )
        )
    )

    return send_file(map.render())

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(host='0.0.0.0', debug=options.debug, port=heroku_port)
