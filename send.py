import pika

credentials = pika.PlainCredentials("admin","adminadmin")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost",port="5672",virtual_host="customers",credentials=credentials))
channel=connection.channel()

channel.queue_declare(queue="hello")
channel.basic_publish(exchange="",routing_key="hello",body="Hello World!")

print("[x] sent Hello World!")
connection.close()