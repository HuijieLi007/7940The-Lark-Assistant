import redis
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

provinceNumberKey = 'province-number'

# fill in the following.
HOST = "redis-13199.c99.us-east-1-4.ec2.cloud.redislabs.com"
PWD = "1Eqc9RPc50181XL2Yk2E1PkGsvqz3Qlh"
PORT = "13199" 

r = redis.Redis(host = HOST, password = PWD, port = PORT, decode_responses = True)

def getMap():
	# load data from redis
    number = r.get(provinceNumberKey)
    data_pair = []
    for i in range(0, int(number)):
        key = 'province-data-' + str(i)
        data_pair.append([
                        r.hget(key, 'province_cn'),
                        r.hget(key, 'number'),
        	        ])

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
                                height='600px',
            page_title='coronavirus-map',

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
                                                range_color = range_color
                                           ),
            title_opts = opts.TitleOpts(title='coronavirus-map')
        )
    )

    return map.render()

def loadMapToRedis():
    df = pd.read_csv('province-number.csv')
    i = 0
    for index, row in df.iterrows():
        key = 'province-data-' + str(i)
        r.hset(key, 'province', row['province'])
        r.hset(key, 'province_cn', row['province_cn'])
        r.hset(key, 'number', row['number'])
        i=i+1

    r.set(provinceNumberKey, i)