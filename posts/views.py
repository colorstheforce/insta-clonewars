from django.shortcuts import render, redirect
from posts.models import Post
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as dlogout
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='/accounts/login/')
def ajaxsavephoto(request):
	ajax = AjaxSavePhoto(request.POST, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

@login_required(login_url='/accounts/login/')
def ajaxlikephoto(request):
	ajax = AjaxLikePhoto(request.GET, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

@login_required(login_url='/accounts/login/')
def ajaxtag(request):
	ajax = AjaxTagPhoto(request.GET, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

@login_required(login_url='/accounts/login/')
def ajaxphotofeed(request):
    ajax = AjaxPhotoFeed(request.GET, request.user)
    context = { 'ajax_output': ajax.output() }
    return render(request, 'ajax.html', context)

@login_required(login_url='/accounts/login/')
def ajaximage(request):
    ajax = AjaxPhotoComments(request.GET, request.user)
    context = { 'ajax_output': ajax.output() }
    return render(request, 'ajax.html', context)

@login_required(login_url='/accounts/login/')
def home(request):
	context = {}
	if request.user.is_authenticated:
		u = User.objects.filter(username=request.user.username)[0]
		if u.userprofiledata.avatar == "":
			u.userprofiledata.avatar = "static/images/avatar.png"
		context = { 'user': request.user, 'ProfilePic': u.userprofiledata.avatar }
		return render(request, 'post/homepage.html', context)

@login_required(login_url='/accounts/login/')
def image(request, pid):
	u = User.objects.filter(username=request.user.username)[0]
	if u.userprofiledata.avatar == "":
		u.userprofiledata.avatar = "static/images/avatar.png"
	try:
		pic=Post.objects.get(id=pid)
	except ObjectDoesNotExist:
		pic=None

	context = {"user":u,"pic":pic,'ProfilePic': u.userprofiledata.avatar}
	return render(request, 'post/image.html',context)
