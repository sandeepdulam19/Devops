from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis

# Initialize the Flask app
app = Flask(__name__)

# Configure the database URI (PostgreSQL in this case)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgre:123456789@database:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Connect to Redis (host is the name of the cache service in Docker Compose)
cache = redis.StrictRedis(host='cache', port=6379, db=0)

@app.route('/')
def hello():
    return 'Hello from Flask! This is Sandeep Dulam'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
