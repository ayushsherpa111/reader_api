""" The main entry point for the API  """
from os import getenv
from src import app

if __name__ == "__main__":
    app.run(debug=getenv("FLASK_ENV") == "development")
