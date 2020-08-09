""" The main entry point for the API  """
from os import getenv
from src import create_app
from dotenv import load_dotenv
from src.models.manga import db
load_dotenv(verbose=True,
            dotenv_path=__import__("pathlib").Path(".")/'.flaskenv')
app = create_app()
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URL")
print(getenv("DB_URL"))

if __name__ == "__main__":
    app.run(debug=getenv("FLASK_ENV") == "development")
