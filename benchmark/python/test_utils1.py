from messages_pb2 import *
import time
import requests
import kafka

import threading

mess = Message()
mess.client.hash.append(1)
mess.type = Message.SELECT

def test(mess):
	info = requests.get(f'http://localhost:8080/info?id={mess.client.id}')
	info = RestResponse.FromString(info.content)

	def _consumer():
		consumer = kafka.KafkaConsumer(info.hashed_id, group_id='worker',
										bootstrap_servers=info.broker_address,
										auto_offset_reset="earliest")
		for i in consumer:
			print(i)
			break
		consumer.close()

	def _producer():
		requests.post('http://localhost:8080/query', data=mess.SerializeToString())

	admin = kafka.KafkaAdminClient(bootstrap_servers=info.broker_address)
	try:
		admin.create_topics([kafka.admin.NewTopic(info.hashed_id, 1, 1)])
		pass
	except Exception as e:
		print(e)

	_producer()
	_consumer(start)

	admin.delete_topics([info.hashed_id])
	admin.close()


re = []
for i in range(1000):
	 print(i)
	 mess.client.id = i
	 print(mess)
	 start = time.time()
	 test(mess)
	 end = time.time()
	 re.append(end - start)

print()
print("Avg: ", sum(re) / len(re))
print("Max: ", max(re))
print(re)