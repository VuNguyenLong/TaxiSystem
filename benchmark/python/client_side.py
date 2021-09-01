from messages_pb2 import *
import h3.api.basic_int as h3
import requests
import kafka
import numpy as np
from functools import *
import json
import time

CLIENT_ID = 1

# Initial session
info = requests.get(f'http://localhost:8080/info?id={CLIENT_ID}')
info = RestResponse.FromString(info.content)
consumer = kafka.KafkaConsumer(info.hashed_id, group_id='worker',
                                bootstrap_servers=info.broker_address,
                                auto_offset_reset="earliest",
                                consumer_timeout_ms=5000)

admin = kafka.KafkaAdminClient(bootstrap_servers=info.broker_address)
try:
    admin.create_topics([kafka.admin.NewTopic(info.hashed_id, 1, 1)])
except Exception as e:
    print(e)


# Begin services loop
def services():
    def to_query(response:Response, x, y):
        HOST = 'http://127.0.0.1:8000/'
        QUERY = 'table/v1/driving/'
        suffix = '?sources=0&annotations=distance'

        locations = reduce(lambda x, y: x + '{},{};'.format(y.lat, y.long), response.response.drivers, '{},{};'.format(y, x))
        return HOST + QUERY + locations[:-1] + suffix

    def retrieve(response: Response, x, y, k):
        if not response.response.drivers:
            return []

        osrm_reply = requests.get(to_query(response, x, y)).content
        distance = json.loads(osrm_reply)['distances'][0][1:]
        return sorted(zip(response.response.drivers, distance), key=lambda x: x[1])[:k]


    # Message preparation
    mess = Message()
    mess.type = Message.SELECT
    mess.client.id = CLIENT_ID

    x = np.random.uniform(low=10.361150797591193, high=11.14905794904022)
    y = np.random.uniform(low=106.59572659658203, high=106.67503415273437)
    resolution = 7
    hash_0 = h3.geo_to_h3(x, y, resolution)
    mess.client.hash.append(hash_0)

    vehicle_type = np.random.randint(1, 10)
    mess.client.vehicle_type = vehicle_type

    print(f'x = {x}\ny = {y}\nhash = {hash_0}\nresolution = {resolution}\nvehicle type = {vehicle_type}\n')

    def _consumer():
        for val in consumer:
            return retrieve(Response.FromString(val.value), x, y, k = 5)

    def _producer():
        requests.post('http://localhost:8080/query', data=mess.SerializeToString())

    _producer()
    result = _consumer()


    # display result to client application
    def format(y):
        return  f'driver id = {y[0].id}\n' + \
                f'\tx = {y[0].long}\n' + \
                f'\ty = {y[0].lat}\n' + \
                f'\td = {y[1]}'
    print(reduce(lambda x, y: x + format(y) + '\n', result, ''))

elapsed_time = []
for i in range(10):
    start = time.time()
    print(f'\n\nrequest {i}')
    services()
    end = time.time()
    print(f'Elapsed time {end - start:.4f}s')
    elapsed_time.append(end - start)

print(f'Average elapsed time {sum(elapsed_time) / len(elapsed_time):.4f}s')


# Finalize session
consumer.close()
# admin.delete_topics([info.hashed_id])
admin.close()