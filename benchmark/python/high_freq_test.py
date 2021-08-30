from messages_pb2 import *
import h3.api.basic_int as h3
import time
import requests
import kafka
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mess_count = 0
interval = 0
N = 2500

records = {}
consumer = kafka.KafkaConsumer("benchmark", group_id='worker',
                                   bootstrap_servers=["localhost:9092"],
                                   auto_offset_reset="earliest",
                                   consumer_timeout_ms=5000)
info = requests.get(f'http://localhost:8080/info?id={0}')
info = RestResponse.FromString(info.content)

size = 4
full = [0] * size
progress = [0] * size

def _consumer():
    global mess_count
    global interval
    start = time.time()
    for i in consumer:
        data = Response.FromString(i.value)
        records[data.client_id][1] = float(data.timestamp)
        end = time.time()

        mess_count += 1
        interval += end - start

        if mess_count >= N * size:
            break

        start = time.time()

import threading
thread = threading.Thread(target=_consumer)
thread.start()


def test(mess):
    global records
    records[mess.client.id] = [time.time() * 1000, 0]
    requests.post('http://localhost:8080/query', data=mess.SerializeToString())

def multi_test(ID):
    global full
    global progress
    for i in range(ID * N, (ID + 1) * N):
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

        start = time.time()
        test(mess)
        end = time.time()

        full[ID] += end - start
        progress[ID] += 1

threads = list(map(lambda i: threading.Thread(target=multi_test, args=(i, )), range(size)))
[i.start() for i in threads]

while mess_count < N * size:
    print('\rf = {:.6f},\tprogress = {}/{},\treceive_progress = {}/{}'
          .format(sum(progress) / (sum(full) + 1e-6), sum(progress), N*size, mess_count, N * size)
          , flush=True, end='')
    time.sleep(0.1)

print()
[i.join() for i in threads]
thread.join()
print("done")

data = pd.DataFrame(records).values.T
data = pd.DataFrame(np.c_[data[:, 0], data[:, 1], data[:, 1] - data[:, 0]], columns=['start', 'end', 'delta'])
data.to_csv(f'result_n={size}_f=70_{N}_v2.csv')

print(data.describe())
plt.hist(data['delta'])
plt.show()