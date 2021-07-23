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

	start = [False]
	def _consumer(lock):
		consumer = kafka.KafkaConsumer(info.hashed_id, group_id='worker',
										bootstrap_servers=info.broker_address,
										auto_offset_reset="earliest")
		for i in consumer:
			print(i)
			break
		consumer.close()
		lock[0] = True

	def _producer():
		requests.post('http://localhost:8080/query', data=mess.SerializeToString())

	def _producer_wrapper(lock):
		n = 0
		_producer()
		while not lock[0]:
			time.sleep(10)
			_producer()
			n += 1
		print('retry ' + str(n))

	admin = kafka.KafkaAdminClient(bootstrap_servers=info.broker_address)
	try:
		admin.create_topics([kafka.admin.NewTopic(info.hashed_id, 1, 1)])
		pass
	except Exception as e:
		print(e)

	thread = threading.Thread(target=_producer_wrapper, args=(start, ))
	thread.start()
	_consumer(start)
	thread.join()

	#admin.delete_topics([info.hashed_id])
	admin.close()


re = []
for i in range(129):
	 print(i)
	 mess.client.id = i
	 print(mess)
	 start = time.time()
	 test(mess)
	 end = time.time()
	 re.append(end - start)