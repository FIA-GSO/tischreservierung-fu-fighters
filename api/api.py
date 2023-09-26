import flask
from flask import request   # wird benötigt, um die HTTP-Parameter abzufragen
from flask import jsonify   # übersetzt python-dicts in json
from . import create_app

app = create_app

@app.route('/', methods=['GET'])
def reserveTable():
    return "Hello"    

app.run()