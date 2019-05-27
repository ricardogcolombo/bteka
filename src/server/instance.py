from flask import Flask

from flask_restplus import Api
from ..models import db
from .settings import DBUSER, DBPASS, DBHOST, DBNAME

#  from sqlalchemy import create_engine

from flask_cors import CORS


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = (
            "mysql://"
            + str(DBUSER)
            + ":"
            + str(DBPASS)
            + "@"
            + str(DBHOST)
            + "/"
            + str(DBNAME)
        )
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.app.config["SESSION_COOKIE_SECURE"] = True
        self.app.config["SESSION_COOKIE_NAME"] = "bteka"
        self.api = Api(self.app, version="1.0", title="Information API")
        db.init_app(self.app)


server = Server()
