import pika

def callback(ch, method, properties, body):
    print("Received " + body.decode("utf-8") )

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='random_numbers')

channel.basic_consume(callback,
                      queue='random_numbers',
                      no_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()