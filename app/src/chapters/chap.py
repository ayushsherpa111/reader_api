""" The route related to all Chapters for the Manage """
from flask_restful import Resource
from src.models.manga import Manga, db


class Chapter(Resource):
    def get(self):
        with open("assets/summary.txt", "r") as summary:
            return {"summary": summary.read(), "test": "test"}, 200, \
                {'access-control-allow-origin': "http://localhost:3000"}

    def post(self):
        newManga = Manga(chapter_count=10)
        db.session.add(newManga)
        db.session.commit()
        print(newManga)
        return {"done": True}
