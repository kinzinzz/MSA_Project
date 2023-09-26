from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_cors import CORS
import requests
import os

# DB connection environment variable
user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
database = os.environ.get("POSTGRES_DB")
host = os.environ.get("POSTGRES_HOST")
port = os.environ.get("POSTGRES_PORT")

# connection to postgres
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

    def serialize(self):
        return {
        'id': self.id,
        'title': self.title,
        'image': self.image
    }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'post_id', name='user_post_unique')

@app.route('/api/post')
def index():
    posts = db.session.query(Post).all()
    serialized_posts = [post.serialize() for post in posts]
    return jsonify(serialized_posts)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')