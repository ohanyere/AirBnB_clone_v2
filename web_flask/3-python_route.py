#!/usr/bin/python3
'''
    contains the hello HBNB functions
'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''prints hello HBNB to screen'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''displays just HBNB'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def user_text(text):
    '''displays c with a text'''
    return 'C {}'. format(text.replace('_', ' '))


@app.route("/python/<text>", strict_slashes=False)
def pyth_txt(text="is cool"):
    '''displays python with a text'''
    return 'Python {}'. format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
