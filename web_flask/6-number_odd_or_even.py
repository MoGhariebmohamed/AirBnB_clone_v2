#!/usr/bin/python3
"""
to start flask in 0.0.0.0:5000
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_flask():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_flask(text):
    return "C " + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
def python_flask():
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def pythondir_flask(text):
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def pythonint_flask(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_flask(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def html_oddevenflask(n):
    if (n % 2 == 0):
        odd_evenstate = 'even'
    else:
        odd_evenstate = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           odd_evenstate=odd_evenstate)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
