import pika
import json
import time
import statistics

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='test_queue')

latencies = []

def callback(ch, method, properties, body):
    message = json.loads(body)
    received_time = time.time()
    latency = received_time - message['timestamp']
    latencies.append(latency)
    print(f"Message {message['id']} received with latency {latency:.4f} seconds")

    if len(latencies) >= 1000:  
        channel.stop_consuming()

channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()

if latencies:
    avg_latency = statistics.mean(latencies)
    max_latency = max(latencies)
    min_latency = min(latencies)
    print(f"Average Latency: {avg_latency:.4f} seconds")
    print(f"Max Latency: {max_latency:.4f} seconds")
    print(f"Min Latency: {min_latency:.4f} seconds")

connection.close()
