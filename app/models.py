from werkzeug.security import generate_password_hash, check_password_hash

from app import db


ROLE_USER = 0
ROLE_ADMIN = 1


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    pw_hash = db.Column(db.String)
    description = db.Column(db.String(2000))
    location = db.Column(db.String)
    feedback = db.relationship('Feedback', backref='university', lazy='dynamic')

    def __repr__(self):
        return 'Bla bla %r' % self.name

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def get_score(self):
        return 9


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    body = db.Column(db.String)
    rating = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=db.func.now())
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'))

    @staticmethod
    def save_feedback(name, body, rating, university_id):
        university = University.query.get(university_id)
        feedback = Feedback(name=name, body=body, rating=rating, university=university)
        db.session.add(feedback)
        db.session.commit()
        return feedback

    @staticmethod
    def delete_feedback(feedback_id):
        post = Feedback.query.get(feedback_id)
        db.session.delete(post)
        db.session.commit()

#