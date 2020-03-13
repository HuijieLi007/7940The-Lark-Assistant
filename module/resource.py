import redis
import pandas as pd


# fill in the following.
HOST = "redis-13199.c99.us-east-1-4.ec2.cloud.redislabs.com"
PWD = "1Eqc9RPc50181XL2Yk2E1PkGsvqz3Qlh"
PORT = "13199" 

r = redis.Redis(host = HOST, password = PWD, port = PORT, decode_responses = True)

def getResource():
    resource = []
    for i in range(1, 11):
        key = 'health-resource-' + str(i)
        resource.append({
                            'title': r.hget(key, 'title'),
                            'src': r.hget(key, 'src'),
                            'image': r.hget(key, 'image'),
                            'type': r.hget(key, 'type'),
                        })

    return resource

def loadDataToRedis():
    df = pd.read_csv('products.csv')
    for index, row in df.iterrows():
        key = 'health-resource-' + str(row['id'])
        r.hset(key, 'id', row['id'])
        r.hset(key, 'title', row['title'])
        r.hset(key, 'src', row['src'])
        r.hset(key, 'image', row['image'])
        r.hset(key, 'type', row['type'])
