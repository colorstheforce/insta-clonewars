from django.test import TestCase
from django.contrib.auth.models import User

class TestUser(TestCase):
    def setUp(self):
        self.testuser=User(username="user",email="test@mail.com")


    def test_instance(self):
        self.assertIsInstance(self.testuser,User)

    def test_save_user(self):
        self.assertFalse(self.testuser in User.objects.all())
        self.testuser.save()
        self.assertTrue(self.testuser in User.objects.all())
        self.testuser.delete()

    def test_delete_user(self):
        self.testuser.save()
        self.assertTrue(self.testuser in User.objects.all())
        self.testuser.delete()
        self.assertFalse(self.testuser in User.objects.all())

    def test_pass_check(self):
        self.testuser.set_password('password')
        self.assertTrue(self.testuser.check_password('password'))
        
    

