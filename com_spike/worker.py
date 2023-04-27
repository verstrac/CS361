# Caleb Verstraete
# 4/26/23
# RabbitMQ tutorial. Worker to receive messages and print the message received. Can start multiple workers to handle
# more load.
import pika, time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print('[*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print("[x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print("[x] Done")
    # Don't forget the basic_ack. Can cause problems where server continuously sends out messages because
    # of no message acknowledgement.
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
