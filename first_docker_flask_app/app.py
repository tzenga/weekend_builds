from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    text = 'You hit the index page'
    return render_template('index.html', text=text)

@app.route('/test_rest')
def test():
    return render_template('index.html',text = 'testing 1 2 3')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
