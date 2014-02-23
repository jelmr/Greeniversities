from werkzeug.security import generate_password_hash, check_password_hash

from app import db


ROLE_USER = 0
ROLE_UNIVERSITY = 1
ROLE_ADMIN = 2


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    pw_hash = db.Column(db.String)
    description = db.Column(db.String(2000))
    location = db.Column(db.String)
    feedback = db.relationship('Feedback', backref='university', lazy='dynamic')

    def __init__(self, name, username, password, description, location):
        self.update(name, username, password, description, location)

    def __repr__(self):
        return 'Bla bla %r' % self.name

    def set_password(self, password):
        if password != "":  # allow submitting form without changing password
            self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def get_score(self):
        return 9

    def update(self, name, username, password, description, location):
        self.name = name
        self.username = username
        self.set_password(password)
        self.description = description
        self.location = location
        db.session.commit()

    @staticmethod
    def delete_university(university_id):
        university = University.query.get(university_id)
        db.session.delete(university)
        db.session.commit()


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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    pw_hash = db.Column(db.String)
    mail = db.Column(db.String(120), unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __init__(self, username, password, mail, role=ROLE_USER):
        self.username = username
        self.set_password(password)
        self.mail = mail
        self.role = role

    def set_password(self, password):
        if password != "":  # allow submitting form without changing password
            self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
