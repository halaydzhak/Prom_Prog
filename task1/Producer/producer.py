#!/usr/bin/env python3
import pika
from random import random
import time

connection = pika.BlockingConnection(pika.URLParameters(
        "amqp://user:pswd@queue:5672"))
channel = connection.channel()

channel.queue_declare(queue='rndnum')

while True:
    rnd_num = random()
    channel.basic_publish(exchange='',
                        routing_key='rndnum',
                        body=str(rnd_num))
    
    print(" [x] Sent ", rnd_num)
    delay_time = random() * 10
    print()
    print(" [x] Delay Time =", delay_time)
    time.sleep(delay_time)

connection.close()
