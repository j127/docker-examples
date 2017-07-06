from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def index():
    count = redis.incr('hits')
    return '''Saluton mondo! Counter: {}.
            Vist the <a href="/something">something page</a>.'''.format(count)


@app.route('/something')
def something():
    about_hits = redis.incr('about_hits')
    return 'something page got {} hits. <a href="/">return home</a>' \
            .format(about_hits)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
