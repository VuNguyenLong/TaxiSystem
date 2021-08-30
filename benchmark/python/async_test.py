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
N = 10000

records = {}
consumer = kafka.KafkaConsumer("benchmark", group_id='worker',
                                   bootstrap_servers=["localhost:9092"],
                                   auto_offset_reset="earliest",
                                   consumer_timeout_ms=5000)
info = requests.get(f'http://localhost:8080/info?id={0}')
info = RestResponse.FromString(info.content)

def _consumer():
    global mess_count
    global interval
    start = time.time()
    for i in consumer:
        data = Response.FromString(i.value)
        records[data.client_id][1] = float(data.timestamp)
        records[data.client_id][2] = time.time() * 1000
        end = time.time()

        mess_count += 1
        interval += end - start

        if mess_count >= N:
            break

        start = time.time()

import threading
thread = threading.Thread(target=_consumer)
thread.start()

def test(mess):
    records[mess.client.id] = [time.time() * 1000, 0, 0]
    requests.post('http://localhost:8080/query', data=mess.SerializeToString())

full = 0
for i in range(N):
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
    #time.sleep(0.01)
    end = time.time()

    full += end - start

    print("\rf = {:.6f},\tsend_progress = {:.6f}%\treceive_progress = {}/{}".format((i + 1) / full, i / N * 100, mess_count, N), flush=True, end='')

start = time.time()
print()
while mess_count < N:
    print('\rreceive_progress = {}/{}'.format(mess_count, N), flush=True, end='')
    if time.time() - start > 10:
        break
    else:
        time.sleep(0.1)
print()
thread.join()
print("done")
data = pd.DataFrame(records).values.T
data = pd.DataFrame(np.c_[data[:, 0], data[:, 1], data[:, 2], data[:, 1] - data[:, 0], data[:, 2] - data[:, 0]], columns=['start', 'sys', 'actual', 'delta_sys', 'delta_actual'])
data.to_csv(f'result_f=100_{N}_v2.csv')

print(data.describe())
plt.hist(data['delta_actual'])
plt.show()