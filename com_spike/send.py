# Caleb Verstraete
# 4/25/2023
# Trying RabbitMQ for communication between Services Hello World Send File
# Copied from: https://www.rabbitmq.com/tutorials/tutorial-one-python.html, 4/25/23
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.basic_publish(exchange='', routing_key='hello', body='A message from CS361')
print("[x] Sent 'A message from CS361'")
connection.close()
