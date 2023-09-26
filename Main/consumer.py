
import pika, json
from app import Post, db, app

params = pika.URLParameters("amqps://govrtnay:tMnQn4JaY1ZzT3J_ErPMtABxqMMSiW9V@dingo.rmq.cloudamqp.com/govrtnay")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='app')

def callback(ch, method, properties, body):
    print('Received in app')
    data = json.loads(body)
    print(data)
    
    with app.app_context():
        
        if properties.content_type == 'post_created':
            post = Post(id=data['id'], title=data['title'], image=data['image'])
            db.session.add(post)
            db.session.commit()
            print('Post Created')
            
        elif properties.content_type == 'post_updated':
            post = Post.query.get(data['id'])
            post.title = data['title']
            post.image = data['image']
            db.session.commit()
            print('Post Updated')
            
        elif properties.content_type == 'post_deleted':
            post = Post.query.get(data)
            db.session.delete(post)
            db.session.commit()        
            print('Post Deleted')
            
    channel.basic_ack(delivery_tag=method.delivery_tag)
    
channel.basic_consume(queue='app', 
                      on_message_callback=callback,
                      auto_ack=False)

print('Started Consuming')

channel.start_consuming()

channel.close()

