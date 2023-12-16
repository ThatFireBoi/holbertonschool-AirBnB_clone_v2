#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of states"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


@app.route('/states')
def states():
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_id(id):
    states = storage.all(State).values()
    state = next((state for state in states if state.id == id), None)
    if state is not None:
        cities = sorted(state.cities, key=lambda city: city.name)
    else:
        cities = []
    return render_template('9-states.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """Close storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
