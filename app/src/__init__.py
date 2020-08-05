from flask import Flask
from src.episode.routes import episode

def create_app():
    app = Flask(__name__)
    app.register_blueprint(episode)
    return app
