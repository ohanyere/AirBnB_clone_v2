#!/usr/bin/python3
'''
    contains the hello HBNB function
'''

from flask import Flask

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    '''prints hello HBNB to screen'''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
