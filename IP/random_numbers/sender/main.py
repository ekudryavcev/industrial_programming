import pika, random, time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='random_numbers')

print('Sending random numbers. To exit press CTRL+C')
try:
    while True:
        channel.basic_publish(exchange='',
                              routing_key='random_numbers',
                              body=str(random.randint(0, 100)))
        time.sleep(random.randint(0, 5))
finally:
    connection.close()
print('Stopped sending numbers.')