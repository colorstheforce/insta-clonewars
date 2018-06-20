from django import forms
from django.contrib.auth import authenticate
from django.db.models import F
from django.contrib.auth.models import User
from posts.models import Post, PhotoLikes,PhotoTag
from userprofile.models import Followers
from urllib.request import urlopen
from random import randint

import json, re

class Ajax(forms.Form):
	args = []
	user = []

	def __init__(self, *args, **kwargs):

		self.args = args
		if len(args) > 1:
			self.user = args[1]
			if self.user.id == None:
				self.user = "NL"

	def error(self, message):
		return json.dumps({ "Status": "Error", "Message": message }, ensure_ascii=False)

	def success(self, message):
		return json.dumps({ "Status": "Success", "Message": message }, ensure_ascii=False)

	def likes(self, message,pid,likes):
		return json.dumps({ "Status": "Success", "Message": message, "pid":pid ,"likes":likes }, ensure_ascii=False)

	def items(self, json):
		return json

	def output(self):
		return self.validate()


class AjaxSavePhoto(Ajax):
	def validate(self):
		try:
			self.url = self.args[0]["url"]
			self.baseurl = self.args[0]["baseurl"]
			self.caption = self.args[0]["caption"]
		except Exception as e:
			return self.error("Malformed request, did not process.")

		if self.user == "NL":
			return self.error("Unauthorised request.")

		if len(self.caption) > 140:
				return self.error("Caption must be 140 characters.")

		if self.url[0:20] != "https://ucarecdn.com" or self.baseurl[0:20] != "https://ucarecdn.com":
			return self.error("Invalid image URL")

		result = urlopen(self.baseurl+"-/preview/-/main_colors/3/")
		data = result.read()
		data = json.loads(data.decode('utf-8'))

		main_colour = ""
		if data["main_colors"] != []:
			#main_colour = data["main_colors"][randint(0, 2)]
			for colour in data["main_colors"][randint(0, 2)]:
				main_colour = main_colour + str(colour) + ","
			main_colour = main_colour[:-1]

		result = urlopen(self.baseurl+"detect_faces/")
		data = result.read()
		data = json.loads(data.decode('utf-8'))

		tag_count = 0
		p = Post(url=self.url, baseurl=self.baseurl, user=self.user, likes=0, caption=self.caption, main_colour=main_colour)

		p.save()
		if data["faces"] != []:
			for face in data["faces"]:
				tag = PhotoTag(photoid=p.id, coords=face).save()
		tag_count = len(data["faces"])
		p.tags = tag_count
		p.save()

		return self.success("Image Uploaded")

class AjaxLikePhoto(Ajax):
	def validate(self):
		try:
			self.postid = self.args[0]["id"]
		except Exception as e:
			return self.error("Malformed request, did not process.")

		if self.user == "NL":
			return self.error("Unauthorised request.")

		if not PhotoLikes.objects.filter(liker=self.user.username, postid=self.postid).exists():
			Post.objects.filter(id=self.postid).update(likes=F('likes')+1)
			like = PhotoLikes(postid=self.postid, liker=self.user.username)
			like.save()
		else:
			Post.objects.filter(id=self.postid).update(likes=F('likes')-1)
			PhotoLikes.objects.filter(postid=self.postid, liker=self.user.username).delete()
		like_count=Post.objects.filter(id=self.postid)[0].likes

		return self.likes("Photo Liked!",self.postid,like_count)

class AjaxPhotoFeed(Ajax):
    def validate(self):
        try:
            self.start = self.args[0]["start"]
        except Exception as e:
            return self.error("Malformed request, did not process.")
        out = []
        followerslist = [self.user]
        profilepics = {}

        for follower in self.user.userprofiledata.following.all():
            followerslist.append(follower)

        for user in User.objects.filter(username__in=followerslist):
            profilepics[user.username] = user.userprofiledata.avatar
            if user.userprofiledata.avatar == "":
                profilepics[user.username] = "https://imgur.com/jVr43h8.png"

        for item in Post.objects.filter(user__in=followerslist).order_by('-date_uploaded')[int(self.start):int(self.start)+3]:
            if PhotoLikes.objects.filter(liker=self.user.username).filter(postid=item.id).exists():
                liked = True
            else:
                liked = False  
            owner=item.user.username          
            out.append({ "PostID": item.id, "URL": item.url, "Caption": item.caption, "Owner": owner, "Likes": item.likes, "DateUploaded": item.date_uploaded.strftime("%Y-%m-%d %H:%M:%S"), "Liked": liked, "ProfilePic": profilepics[owner]+"", "MainColour": item.main_colour })

        return self.items(json.dumps(out))

class AjaxPhotoComments(Ajax):
	def validate(self):
		try:
			self.image_id,owner = int(self.args[0]["image_id"]),self.user.username
			self.start = self.args[0]["start"]
		except Exception as e:
			return self.error("Malformed request, did not process.")
		out = []
		followerslist = [self.user.username]
		profilepics = {}

		for follower in self.user.userprofiledata.following.all():
			followerslist.append(follower)

		for user in User.objects.filter(username__in=followerslist):
			profilepics[user.username] = user.userprofiledata.avatar
			if user.userprofiledata.avatar == "":
				profilepics[user.username] = "https://imgur.com/jVr43h8.png"

		for item in Post.objects.filter(id=self.image_id).order_by('-date_uploaded')[int(self.start):int(self.start)+3]:
			if PhotoLikes.objects.filter(liker=self.user.username).filter(postid=item.id).exists():
				liked = True
			else:
				liked = False
			out.append({ "PostID": item.id, "URL": item.url, "Caption": item.caption, "Owner": owner, "Likes": item.likes, "DateUploaded": item.date_uploaded.strftime("%Y-%m-%d %H:%M:%S"), "Liked": liked, "ProfilePic": profilepics[owner]+"", "MainColour": item.main_colour })

		return self.items(json.dumps(out))

class AjaxTagPhoto(Ajax):
	def validate(self):
		try:
			self.follower = self.args[0]["user"]
		except Exception as e:
			return self.error("Malformed request, did not process.")
