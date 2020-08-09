from src import db


class Manga(db.Model):
    __tablename__ = "manga"
    chapter_id = db.Column(db.Integer, primary_key=True)
    chapter_count = db.Column(db.Integer, nullable=False)
    images = db.relationship("Images", backref="chapters", lazy=True)

    def __init__(self, chapter_count):
        self.chapter_count = chapter_count

    def __repr__(self):
        return f"Manga({self.chapter_id},{self.chapter_count})"


class Images(db.Model):
    manga_id = db.Column(db.Integer, db.ForeignKey("manga.chapter_id"),
                         nullable=False, primary_key=True)
    image_name = db.Column(db.String, primary_key=True)
