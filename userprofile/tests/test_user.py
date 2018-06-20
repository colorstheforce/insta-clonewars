from django.test import TestCase
from django.contrib.auth.models import User

class TestUser(TestCase):
    def setUp(self):
        self.testuser=User(username="user",email="test@mail.com")


    def test_instance(self):
        self.assertEqual(isinstance(self.testuser,User),True)

    def test_save_user(self):
        self.assertEqual(self.testuser in User.objects.all(),False)
        self.testuser.save()
        self.assertEqual(self.testuser in User.objects.all(),True)
        self.testuser.delete()

    def test_delete_user(self):
        self.testuser.save()
        self.assertEqual(self.testuser in User.objects.all(),True)
        self.testuser.delete()
        self.assertEqual(self.testuser in User.objects.all(),False)

    def test_pass_check(self):
        self.testuser.set_password('password')
        self.assertEqual(self.testuser.check_password('password'),True)
        
    

