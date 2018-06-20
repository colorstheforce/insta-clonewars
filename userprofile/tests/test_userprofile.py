from django.test import TestCase
from django.contrib.auth.models import User
from userprofile.models import UserProfileData
'''
assertEqual(a, b)	a == b	 
assertNotEqual(a, b)	a != b	 
assertTrue(x)	bool(x) is True	 
assertFalse(x)	bool(x) is False	 
assertIs(a, b)	a is b	3.1
assertIsNot(a, b)	a is not b	3.1
assertIsNone(x)	x is None	3.1
assertIsNotNone(x)	x is not None	3.1
assertIn(a, b)	a in b	3.1
assertNotIn(a, b)	a not in b	3.1
assertIsInstance(a, b)	isinstance(a, b)	3.2
assertNotIsInstance(a, b)
'''

class TestUserProfile(TestCase):
    def setUp(self):
        self.testuser=User(username="user",email="test@mail.com")
        self.testuser.save()
        UserProfileData.objects.create(user=self.testuser)
        self.testprofile=UserProfileData.objects.filter(user=self.testuser)[0]

        self.followuser=User(username="follower",email="follower@mail.com")
        self.followuser.save()
        UserProfileData.objects.create(user=self.followuser)
        self.followprofile=UserProfileData.objects.filter(user=self.followuser)[0]



    def test_instance(self):
        self.assertIsInstance(self.testprofile,UserProfileData)
    
    def test_string_representation(self):
        self.assertEqual(str(self.testprofile),self.testprofile.user.username)

    def test_delete_profile(self):
        self.assertIn(self.testprofile,UserProfileData.objects.all())
        self.testprofile.delete_userprofile()
        self.assertNotIn(self.testprofile,UserProfileData.objects.all())

    def test_save_profile(self):
        self.fuser=User(username="fuser",email="fuser@mail.com")
        self.fuser.save()
        self.fprofile=UserProfileData(user=self.fuser)
        self.assertNotIn(self.fprofile, UserProfileData.objects.all())
        self.fprofile.save()
        self.assertIn(self.fprofile,UserProfileData.objects.all())

    
    def test_is_following(self):
        self.assertFalse(self.testprofile.is_following(self.followuser))
        self.testprofile.follow_user(self.followuser)
        self.assertTrue(self.testprofile.is_following(self.followuser))

    def test_unfollow(self):
        self.testprofile.follow_user(self.followuser)
        self.assertTrue(self.testprofile.is_following(self.followuser))
        self.testprofile.unfollow_user(self.followuser)
        self.assertFalse(self.testprofile.is_following(self.followuser))
    
    def test_search_users(self):
        self.assertIn(self.testprofile,UserProfileData.search_users(self.testuser.username))
        

        

        
  
        

    
        
        
