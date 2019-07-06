import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://blepub:blepub@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

channel.queue_declare(queue='mac')

def callback(ch, method, properties, body):
  print(" [x] Received %r" % body)

channel.basic_consume('mac', callback,auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
