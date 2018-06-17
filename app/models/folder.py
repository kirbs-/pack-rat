from app import db


class Folder(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(4000), index=True, unique=True)
    should_sync = db.Column(db.Boolean)

    def __init__(self, path):
        self.path = path