#!/usr/bin/python3
'''
    contains the hello HBNB functions
'''

from flask import Flask
from flask import render_template

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


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyth_txt(text="is cool"):
    '''displays python with a text'''
    return 'Python {}'. format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    '''returns a number text'''
    return "{} is a number". format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
        '''returns a html template'''
        return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_or_even(n):
    if (n % 2 == 0):
        return render_template('6-number_odd_or_even.html', n=n, t="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, t="odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
