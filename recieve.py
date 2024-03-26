import pika
import sys
import os

credentials = pika.PlainCredentials("admin","adminadmin")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost",port="5672",virtual_host="customers",credentials=credentials))
channel=connection.channel()

channel.queue_declare(queue="hello")

def callback(ch,method,properties,body):
    print(f'[x] Recieved {body}')

channel.basic_consume(queue="hello",auto_ack=True,on_message_callback=callback)

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