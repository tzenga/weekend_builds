from flask import Flask, render_template
import random
import time
import redis

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379)

@app.route('/')
def index():
    text = 'You hit the index page'
    count = get_hit_count()
    count_text = 'Hello, you have been seen {} times.\n'.format(count)
    return render_template('index.html', text=text, count=count_text)

@app.route('/test')
def test():
    return render_template('index.html',text = 'testing 1 2 3', count='Count says what?')

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -=1
            time.sleep(0.5)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
