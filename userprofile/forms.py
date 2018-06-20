from django import forms
from .models import UserProfileData
from posts.models import Post,PhotoLikes,PhotoTag
from posts.forms import Ajax
import json, re
from django.contrib.auth.models import User
class EditInfo(forms.ModelForm):
    class Meta:
        model = UserProfileData
        fields = [
            "status",
            "secondary_email",
            "phone_number",
        ]




class AjaxProfileFeed(Ajax):
    def validate(self):
        try:
            self.username = self.args[0]["username"]
            self.puser=User.objects.filter(username=self.username)[0]
            self.start = self.args[0]["start"]

        except Exception as e:
            return self.error("Malformed request, did not process.")
        out = []
        for item in Post.objects.filter(user=self.puser).order_by('-date_uploaded')[int(self.start):int(self.start)+3]:
            if PhotoLikes.objects.filter(liker=self.user.username).filter(postid=item.id).exists():
                liked = True
            else:
                liked = False
            owner=self.puser.username
            out.append({ "PostID": item.id, "URL": item.url, "Caption": item.caption, "Owner": owner, "Likes": item.likes, "DateUploaded": item.date_uploaded.strftime("%Y-%m-%d %H:%M:%S"), "Liked": liked, "MainColour": item.main_colour })

        return self.items(json.dumps(out))

class AjaxSetProfilePic(Ajax):
    def validate(self):
        try:
            self.url = self.args[0]["url"]
            self.baseurl = self.args[0]["baseurl"]
        except Exception as e:
            return self.error("Malformed request, did not process.")

        if self.user == "NL":
            return self.error("Unauthorised request.")

        if self.url[0:20] != "https://ucarecdn.com" or self.baseurl[0:20] != "https://ucarecdn.com":
            return self.error("Invalid image URL")

        u = User.objects.filter(username=self.user.username)[0]
        p= UserProfileData.objects.filter(user=self.user)[0]

        p.avatar=self.url
        p.save()

        return self.success("Profile Image Uploaded")

class AjaxFollow(Ajax):
	def validate(self):
		try:
			self.follower = self.args[0]["user"]
		except Exception as e:
			return self.error("Malformed request, did not process.")

		if self.user == "NL":
			return self.error("Unauthorised request.")

		if self.user.username == self.follower:
				return self.error("Can't follow yourself")

		if not Followers.objects.filter(user=self.follower,follower=self.user.username).exists():
			f = Followers(user=self.follower, follower=self.user.username).save()
			following = True
		else:
			Followers.objects.filter(user=self.follower, follower=self.user.username).delete()
			following = False
		out = { "Following": following }
		return self.items(json.dumps(out))
