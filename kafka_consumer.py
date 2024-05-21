from kafka import KafkaConsumer
import json
import time
import statistics

consumer = KafkaConsumer('test_topic', bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))

latencies = []
message_count = 0
message_limit = 1000  # Limite de mensajes a procesar

try:
    for message in consumer:
        received_time = time.time()
        latency = received_time - message.value['timestamp']
        latencies.append(latency)
        print(f"Message {message.value['id']} received with latency {latency:.4f} seconds")
        
        message_count += 1
        if message_count >= message_limit:
            break

finally:
    if latencies:
        avg_latency = statistics.mean(latencies)
        max_latency = max(latencies)
        min_latency = min(latencies)
        print(f"Average Latency: {avg_latency:.4f} seconds")
        print(f"Max Latency: {max_latency:.4f} seconds")
        print(f"Min Latency: {min_latency:.4f} seconds")
