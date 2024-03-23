#!/usr/bin/python3
"""
to start flask in 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_flask():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def text_flask(text):
    return "C" + text.replace("_", " ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
