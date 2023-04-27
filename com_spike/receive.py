# Caleb Verstraete
# 4/25/2023
# Trying RabbitMQ for communication between Services Hello World Receive File
# Copied from: https://www.rabbitmq.com/tutorials/tutorial-one-python.html, 4/25/23
import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print("[x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print('[*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit()
        except SystemExit:
            os._exit(0)
