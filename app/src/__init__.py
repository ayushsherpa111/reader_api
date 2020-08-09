""" Initlizer for the API """
from flask import Flask
from flask_restful import Api
from src.chapters.chap import Chapter
from src.models.manga import db


def create_app():
    """ Initialize the app instance for Flask """
    app = Flask(__name__)
    api = Api(app)
    db.init_app(app)
    api.add_resource(Chapter, "/", "/summary")

    return app
