#!/usr/bin/python3
'''This module starts a Flask web application'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Method that returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Method that returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Method that returns C and an inputed text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """Method that returns Python and an inputed text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """Method that returns an integer and a text"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Method that renders a HTML template and an integer"""
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,  debug=True)
