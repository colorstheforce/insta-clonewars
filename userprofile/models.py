#django
from django.db import models
from django.contrib.auth.models import User

class UserProfileData(models.Model):
    class Meta:
        db_table = 'user_profile_data'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name="followers_profile", blank=True)
    following = models.ManyToManyField(User, related_name="following_profile", blank=True)
    status = models.TextField(max_length=100, null=True, blank=True, default="Bangarang!")
    avatar = models.CharField(max_length=255, default="https://imgur.com/jVr43h8.png")
    secondary_email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    
    def save_userprofile(self):
        self.save()
    def delete_userprofile(self):
        self.delete()

    def follow_user(self,follower):
        return self.following.add(follower)

    def unfollow_user(self,to_unfollow):
        return self.following.remove(to_unfollow)
    
    def is_following(self,checkuser):
        return checkuser in self.following.all()

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0
    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0
    
    @classmethod
    def search_users(cls, name):
        profiles = cls.objects.filter(user__username__icontains = name)
        return profiles

    def __str__(self):
        return self.user.username

class Followers(models.Model):
    '''
    deprecated
    '''
    user = models.CharField(max_length=20, default="")
    follower = models.CharField(max_length=20, default="")