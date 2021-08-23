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
    print(i)
    mess = Message()
    mess.type = Message.SELECT
    mess.client.id = i

    y = np.random.uniform(low=-90, high=90)
    x = np.random.uniform(low=-180, high=180)
    resolution = 3
    mess.client.hash.append(h3.geo_to_h3(x, y, resolution))

    print('location {:.6f} {:.6f}'.format(x, y))
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
