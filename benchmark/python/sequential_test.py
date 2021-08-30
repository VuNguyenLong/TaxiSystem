from messages_pb2 import *
import h3.api.basic_int as h3
import time
import requests
import kafka
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def test(mess):
    info = requests.get(f'http://localhost:8080/info?id={mess.client.id}')
    info = RestResponse.FromString(info.content)
    consumer = kafka.KafkaConsumer(info.hashed_id, group_id='worker',
                                   bootstrap_servers=info.broker_address,
                                   auto_offset_reset="earliest",
                                   consumer_timeout_ms=5000)

    def _consumer():
        for i in consumer:
            print(Response.FromString(i.value))
            break
        consumer.close()

    def _producer():
        requests.post('http://localhost:8080/query', data=mess.SerializeToString())

    admin = kafka.KafkaAdminClient(bootstrap_servers=info.broker_address)
    try:
        admin.create_topics([kafka.admin.NewTopic(info.hashed_id, 1, 1)])
    except Exception as e:
        print(e)

    start = time.time()
    _producer()
    _consumer()
    end = time.time()

    #admin.delete_topics([info.hashed_id])
    admin.close()
    return end - start


re = [[], []]
for i in range(1000):
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

    print(mess)
    start = time.time()
    result = test(mess)
    end = time.time()
    re[0].append(result)
    re[1].append(end - start)

print()
dataframe = pd.DataFrame(np.c_[re[0], re[1]], index=range(len(re[0])),
                         columns=['partial request', 'full request'])
print(dataframe.describe())
