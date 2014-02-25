#!flask/bin/python
import os
import sys
import unittest


from config import basedir
from app import app, db
from app.models import User, University
from sqlalchemy.exc import OperationalError


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_make_university(self):
        u = University(name='VU', description='Test', username="test", password="test", location="Amsterdam")
        db.session.add(u)
        db.session.commit()
        university = University.query.get(u.id)
        assert university.name == 'VU'
        assert university.username == 'test'

    def test_university_login(self):
        u = University(name='VU', description='Test', username="test", password="test", location="Amsterdam")
        db.session.add(u)
        db.session.commit()
        university = University.query.get(u.id)
        assert university.check_password('test')

    def test_set_password(self):
        u = University(name='VU', description='Test', username="test", password="test", location="Amsterdam")
        db.session.add(u)
        db.session.commit()
        university = University.query.get(u.id)
        try:
            self.assertRaises(Exception, university.set_password(''))
        except Exception:
            pass

        try:
            university.set_password('test2')
        except Exception:
            self.fail("Fails to set valid password")

        self.assertTrue(university.check_password('test2'))

    def test_get_score(self):
        u = University(name='VU', description='Test', username="test", password="test", location="Amsterdam")
        db.session.add(u)
        db.session.commit()
        university = University.query.get(u.id)
        self.assertEqual(university.get_score(), 9)

    def test_delete_university(self):
        u = University(name='VU', description='Test', username="test", password="test", location="Amsterdam")
        db.session.add(u)
        db.session.commit()
        University.delete_university(u.id)
        u = University.query.get(u.id)
        self.assertIsNone(u)

        
if __name__ == '__main__':
    unittest.main()
