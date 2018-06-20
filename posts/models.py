from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PhotoLikes(models.Model):
	postid = models.IntegerField()
	liker = models.CharField(max_length=20)


class PhotoTag(models.Model):
	photoid = models.IntegerField()
	coords = models.CharField(max_length=20)
	tagged_user = models.CharField(max_length=20, default="")
	tagged_by = models.CharField(max_length=20, default="")


class Post(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, null=True)
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    time_updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    baseurl = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=20)
    likes = models.IntegerField()
    caption = models.CharField(max_length=140, default="")
    tags = models.IntegerField(default=0)
    main_colour = models.CharField(max_length=15, default="")

    def save_pic(self):
        return self.save()

    def delete_pic(self):
        return self.delete()

    def get_number_of_likes(self):
        thelikes=PhotoLikes.objects.filter(postid=self.id).all()
        return thelikes.count()

    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return self.title

class Comments(models.Model):
    comment = models.TextField()
    posted_on = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
    
    @classmethod
    def get_comments_by_images(cls, id):
        comments = cls.objects.filter(image__pk = id)
        return comments