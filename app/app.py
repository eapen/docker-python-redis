import os

from flask import Flask
from redis import Redis


app = Flask(__name__)
bind_port = os.environ['BIND_PORT']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.route('/')
def hello():
    redis.incr('hits')
    return 'Redis ({}) hit counter: {}'.format(REDIS_HOST, redis.get('hits'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
