#!/usr/bin/env python3

from kafka import KafkaProducer
from time import sleep
from json import dumps

server = "localhost:9092"
topic = "greetings"

print("Connecting to Kafka")
producer = KafkaProducer(
    bootstrap_servers=[server],
    value_serializer=lambda x: dumps(x).encode("utf-8")
)
print("Connected to Kafka")

for i in range(1000):
    print(i)
    data = {"counter": i}
    producer.send(topic, value=data)
    sleep(5)
