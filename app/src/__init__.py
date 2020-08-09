""" Initlizer for the API """
from flask import Flask
from os import getenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
db = SQLAlchemy()
app = Flask(__name__)
api = Api(app)

load_dotenv(verbose=True,
            dotenv_path=__import__("pathlib").Path(".")/'.flaskenv')
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# registering routes
from src.chapters.chap import Chapter
api.add_resource(Chapter, "/", "/summary")
