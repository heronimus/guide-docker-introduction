import time

import redis
import socket
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return 'Hello World! I have been seen {} times.<br><br><br>Hostname: {} <br>IP: {}'.format(count,host_name,host_ip)
