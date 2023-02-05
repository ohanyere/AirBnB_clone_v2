#!/usr/bin/python3
'''
    module to start a flask app
'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    '''returns a template of unordered lists of state
        objects
    '''
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def remove_session(self):
    '''
        tears down the session
    '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
