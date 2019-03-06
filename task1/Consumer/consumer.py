#!/usr/bin/env python3
import pika

connection = pika.BlockingConnection(pika.URLParameters(
    	     "amqp://user:pswd@queue:5672"))
channel = connection.channel()

channel.queue_declare(queue='rndnum')

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    # print(" [x] Received %r\n" % (body,))
	f = open('text.txt', 'a')
	f.write(" [x] Received %r\n" % (body,))
	f.close()

channel.basic_consume(callback,
                      queue='rndnum',
                      no_ack=True)

channel.start_consuming()
