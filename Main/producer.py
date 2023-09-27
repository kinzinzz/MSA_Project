import pika, json

params = pika.URLParameters('amqps://govrtnay:tMnQn4JaY1ZzT3J_ErPMtABxqMMSiW9V@dingo.rmq.cloudamqp.com/govrtnay')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    print("publish is working")
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)