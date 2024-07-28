#!/usr/bin/python3
""" Starts a Flash Application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ /: display Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ /hbnb: display “HBNB”  """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ /c/<text>: display “C ” followed by the value of the text variable  """
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
