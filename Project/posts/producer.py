import pika, json

# AMQP url

params = pika.URLParameters("amqps://govrtnay:tMnQn4JaY1ZzT3J_ErPMtABxqMMSiW9V@dingo.rmq.cloudamqp.com/govrtnay")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',
                          routing_key='app',
                          body=json.dumps(body),
                          properties=properties)


