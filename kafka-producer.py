from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for i in range(1000):
    message = {'id': i, 'timestamp': time.time()}
    producer.send('test_topic', value=message)
    time.sleep(0.01)  # Simulate some load
