from main import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), unique=True)
    image = db.Column(db.String(120), unique=True)
    pub_date = db.Column(db.DateTime)
    parsed_at = db.Column(db.DateTime)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<News %r>' % self.title
