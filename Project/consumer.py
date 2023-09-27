# django models import settings for external app, (admin = django project name)
import os
import django 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

# consumer.py
import pika, json
from posts.models import Post

params = pika.URLParameters("amqps://govrtnay:tMnQn4JaY1ZzT3J_ErPMtABxqMMSiW9V@dingo.rmq.cloudamqp.com/govrtnay")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')
print("consumer is working")
def callback(ch, method, properties, body):
    id = json.loads(body)
    print(id)
    post = Post.objects.get(id=id)
    post.likes = post.likes + 1
    post.save()
    print("Post likes increased!")

channel.basic_consume(queue='admin', 
                      on_message_callback=callback,
                      auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

