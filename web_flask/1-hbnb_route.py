#!/usr/bin/python3
'''This module starts a Flask web application'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Method that returns Hello HBNB"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Method that returns HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,  debug=True)
