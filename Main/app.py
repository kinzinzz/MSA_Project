from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'post_id', name='user_post_unique')

@app.route('/api/post')
def index():
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')