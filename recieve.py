import pika
import sys
import os
import time

credentials = pika.PlainCredentials("admin","adminadmin")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost",port="5672",virtual_host="customers",credentials=credentials))
channel=connection.channel()

channel.queue_declare(queue="hello",durable=True)

def callback(ch,method,properties,body):
    print(f'[x] Recieved {body.decode()}')
    time.sleep(body.count(b'.'))
    print("[x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="hello",on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)