from app import db


class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer(), primary_key=True)

    original_link = db.Column(db.String(255), nullable=False, unique=True)
    short_link = db.Column(db.String(255), nullable=False, unique=True)

    counter = db.Column(db.Integer())

    def __repr__(self):
        return "<{} - {}>".format(self.id, self.original_link)
