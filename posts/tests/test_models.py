from django.test import TestCase
from posts.models import Post,PhotoLikes
from django.contrib.auth.models import User

class TestPostLikeModel(TestCase):

    def setUp(self):
        self.testuser=User(username="testuser",email="test@mail.com")
        self.testuser.save()
        self.testpost=Post(user=self.testuser,url="www.example.com/testimage1.jpeg",likes=0)
        self.testpost.save()
        self.testlike=PhotoLikes(postid=self.testpost.id,liker=self.testuser.username)
        self.testlike.save()

    def test_is_instance(self):
        self.assertIsInstance(self.testpost,Post)

    def test_str_post_method(self):
        self.assertEqual(self.testpost.__str__(),self.testpost.url)
    
    def test_str_like_method(self):
        self.assertEqual(self.testlike.__str__(),'liker:{}'.format(self.testlike.liker))
    
    def test_save_delete(self):
        self.testpost2=Post(user=self.testuser,url="www.example.com/testimage2.jpeg",likes=0)
        self.assertNotIn(self.testpost2,Post.objects.all())
        self.testpost2.save_pic()
        self.assertIn(self.testpost2,Post.objects.all())
        self.testpost2.delete()
        self.assertNotIn(self.testpost2,Post.objects.all())

    def test_like_is_instance(self):
        self.assertIsInstance(self.testlike,PhotoLikes)

    def test_like(self):
        self.assertIn(self.testlike,PhotoLikes.objects.all())

    def test_get_like_user(self):
        self.assertEqual(self.testuser,self.testlike.get_user())

    def test_getnumber_of_likes(self):
        self.likes=PhotoLikes.objects.filter(postid=self.testpost.id).count()
        self.assertEqual(self.likes,self.testpost.get_number_of_likes())

    def tearDown(self):
        self.testpost.delete()
        self.testuser.delete()
        self.testlike.delete()


        