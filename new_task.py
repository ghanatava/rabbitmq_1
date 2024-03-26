import pika
import sys 

credentials = pika.PlainCredentials("admin","adminadmin")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost",port="5672",virtual_host="customers",credentials=credentials))
channel=connection.channel()

channel.queue_declare(queue="hello",durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key="hello",
    body=message,
    properties=pika.BasicProperties(
                         delivery_mode = pika.DeliveryMode.Persistent
    )
)

print(f"[x] Sent {message}")

connection.close()
