from app import db


class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer(), primary_key=True)

    long_url = db.Column(db.String(255), nullable=True, unique=True)

    short_link = db.Column(db.String(255), nullable=True, unique=True)
    short_postfix = db.Column(db.String(255), nullable=True, unique=True)

    counter = db.Column(db.Integer(), default=0)

    def __repr__(self):
        return "<{}>".format(self.id)
