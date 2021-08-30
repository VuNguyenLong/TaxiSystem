from messages_pb2 import *
import h3.api.basic_int as h3
import requests
import kafka
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from functools import *
import json

def retrieve(i, x, y, k = 5):
    def to_query(response:Response, x, y):
        if not response.response.drivers:
            return None

        HOST = 'http://127.0.0.1:8000/'
        QUERY = 'table/v1/driving/'
        suffix = '?sources=0&annotations=distance'

        locations = reduce(lambda x, y: x + '{},{};'.format(y.lat, y.long), response.response.drivers, '{},{};'.format(y, x))
        return HOST + QUERY + locations[:-1] + suffix

    def retrieve(response: Response, x, y):
        osrm_reply = requests.get(to_query(response, x, y)).content
        distance = json.loads(osrm_reply)['distances'][0][1:]
        return sorted(zip(response.response.drivers, distance), key=lambda x: x[1])[:k]

    mess = Message()
    mess.type = Message.SELECT
    mess.client.id = i

    x = np.random.uniform(low=10.361150797591193, high=11.14905794904022)
    y = np.random.uniform(low=106.59572659658203, high=106.67503415273437)
    resolution = 7
    hash_0 = h3.geo_to_h3(x, y, resolution)
    mess.client.hash.append(hash_0)

    vehicle_type = np.random.randint(1, 10)
    mess.client.vehicle_type = vehicle_type

    info = requests.get(f'http://localhost:8080/info?id={mess.client.id}')
    info = RestResponse.FromString(info.content)
    consumer = kafka.KafkaConsumer(info.hashed_id, group_id='worker',
                                   bootstrap_servers=info.broker_address,
                                   auto_offset_reset="earliest",
                                   consumer_timeout_ms=5000)

    result = None
    def _consumer():
        global result
        for val in consumer:
            result = retrieve(Response.FromString(val.value), x, y)
            break
        consumer.close()

    def _producer():
        requests.post('http://localhost:8080/query', data=mess.SerializeToString())

    admin = kafka.KafkaAdminClient(bootstrap_servers=info.broker_address)
    try:
        admin.create_topics([kafka.admin.NewTopic(info.hashed_id, 1, 1)])
    except Exception as e:
        print(e)

    _producer()
    _consumer()

    # admin.delete_topics([info.hashed_id])
    admin.close()

    return result

i = 1
x = np.random.uniform(low=10.361150797591193, high=11.14905794904022)
y = np.random.uniform(low=106.59572659658203, high=106.67503415273437)
print(retrieve(i, x, y))
