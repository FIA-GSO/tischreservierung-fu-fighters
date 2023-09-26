import flask

def create_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True  # Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message

    from . import db
    db.init_app(app)

    return app