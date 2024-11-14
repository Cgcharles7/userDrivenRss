import unittest
from app import app
from models import db, User

class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_user_creation(self):
        user = User(username='testuser')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(user.username, 'testuser')
