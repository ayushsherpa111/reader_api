from flask import Blueprint

episode = Blueprint('episode', __name__)


@episode.route("/ep")
def get_all_ep():
    return "EPISODE"
