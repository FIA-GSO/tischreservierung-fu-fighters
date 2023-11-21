import flask
from flask import request   # wird benötigt, um die HTTP-Parameter abzufragen
from flask import jsonify   # übersetzt python-dicts in json

import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True  # Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message

@app.route('/api/v1/', methods=['GET'])
def reserveTable():
    return "<h1>Tischreservierung</h1>"

@app.route('/api/v1/free-tables', methods=['GET'])
def getFreeTables():
    query_parameters = request.args
    date = query_parameters.get('date')

    conn = sqlite3.connect('schema.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    free_tables = cur.execute(
        "SELECT * FROM tische WHERE  tischnummer NOT IN (SELECT tischnummer FROM reservierungen WHERE zeitpunkt BETWEEN datetime(\'" + date + "\', '-30 minutes') AND datetime(\'" + date + "\', '+29 minutes'));"
        ).fetchall()

    return jsonify(free_tables)


@app.route('/api/v1/reservation', methods=['DELETE'])
def cancel_reservation():
    query_parameters = request.args
    table_number = query_parameters.get('table_number')
    date = query_parameters.get('date')

    conn = sqlite3.connect('schema.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    # Siehe Sequenzdiagramm in Mermaid: Der Zeitpunkt muss noch überprüft werden
    # Der Eintrag muss gelöscht werden
    reservation = cur.execute(
        "DELETE * FROM reservierungen WHERE tischnummer = \'" + table_number + "\' AND zeitpunkt = \'" + date + "\';"
        ).delete()

    # Was mache ich hier
    return "Die Reservierung wurde storniert."

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

app.run()