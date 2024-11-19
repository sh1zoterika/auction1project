import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='1')
channel.basic_publish(exchange='',
                      routing_key='1',
                      body='qweewq')
connection.close()