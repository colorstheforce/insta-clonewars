from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from userprofile.models import UserProfileData
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='/accounts/login/')
def index(request):
    if request.user.is_authenticated:
        u=User.objects.get(id=request.user.id)
        try:
            myuser=UserProfileData.objects.get(user=u)
        except ObjectDoesNotExist:
            UserProfileData.objects.create(user=u)

    return HttpResponseRedirect("home")


