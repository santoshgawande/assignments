import pika
credentials = pika.PlainCredentials('blepub', 'blepub')
parameters = pika.ConnectionParameters('127.0.0.1', 25672,'/',credentials)
#print type(parameters)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello W0rld!',durable=True)
print(" [x] Sent 'Hello World!'")
connection.close()

