import pika
import time
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='test_queue')

for i in range(1000):
    message = {'id': i, 'timestamp': time.time()}
    channel.basic_publish(exchange='', routing_key='test_queue', body=json.dumps(message))
    time.sleep(0.01)  # Simulate some load

connection.close()
