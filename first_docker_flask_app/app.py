from flask import Flask, render_template
import random
import time
import graphene
from flask_graphql import GraphQLView
from models import db_session
from schema import schema, Department

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func= GraphQLView.as_view(
        'graphql',
        schema = schema,
        graphiql=True
    )
)

@app.route('/')
def index():
    text = 'You hit the index function'
    count_text = 'You hit this at some num of times'
    return render_template('index.html', text=text, count=count_text)

@app.route('/test')
def test():
    return render_template('index.html',text = 'testing 1 2 3', count='Count says what?')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
