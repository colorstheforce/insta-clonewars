from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from userprofile.models import UserProfileData
from .forms import *
from django.contrib.auth.decorators import login_required
from annoying.decorators import ajax_request


@login_required(login_url='/accounts/login/')
def followers(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfileData.objects.get(user=user)
    profiles = user_profile.followers.all

    context = {
        'header': 'Followers',
        'profiles': profiles,
    }

    return render(request, 'profile/follow_list.html', context)

@login_required(login_url='/accounts/login/')
def following(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfileData.objects.get(user=user)
    profiles= user_profile.following.all()
    context = {
        'header': 'Following',
        'profiles': profiles
    }
    return render(request, 'profile/follow_list.html', context)

@login_required(login_url='/accounts/login/')
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles= UserProfileData.search_users(search_term)
        header = 'Search Results for {}'.format(search_term)
    else:
        profiles=UserProfileData.objects.all()
        header = 'Search Results for all'
    context = {
        'header': header,
        'profiles': profiles
    }
    return render(request, 'profile/search.html', context)



@login_required(login_url='/accounts/login/')
def profile(request, user_username=None):
    if user_username==None:
        user= request.user
    else:
        user = get_object_or_404(User, username=user_username)
    profile = UserProfileData.objects.get(user=user)
    print(profile.id)
    context = {
        'username': user_username,
        'user': user,
        'profile': profile,
        "logged_in_as": request.user.username
    }
    return render(request, 'profile/profile.html', context)


@login_required(login_url='/accounts/login/')
def edit_info(request):
    user_profile_data = UserProfileData.objects.get(user=request.user)
    form = EditInfo(request.POST or None, request.FILES or None, instance=user_profile_data)
    if form.is_valid():
        info = form.save(commit=False)
        info.save()
        return redirect('basic:index')
    return render(request, "profile/edit_info.html", {"form": form})


@ajax_request
@login_required(login_url='/accounts/login/')
def follow_toggle(request):
    user_profile = UserProfileData.objects.get(user=request.user)
    follow_profile_pk = str(int(request.POST.get('follow_profile_pk')))
    print(follow_profile_pk)
    follow_profile = UserProfileData.objects.get(pk=follow_profile_pk)

    try:
        if user_profile != follow_profile:
            if request.POST.get('type') == 'follow':
                user_profile.following.add(follow_profile.user)
                follow_profile.followers.add(user_profile.user)
            elif request.POST.get('type') == 'unfollow':
                user_profile.following.remove(follow_profile.user)
                follow_profile.followers.remove(user_profile.user)
            user_profile.save()
            follow_profile.save()
            result = 1
        else:
            result = 0
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_profile_pk': follow_profile_pk
    }

@login_required(login_url='/accounts/login/')
def ajaxfollow(request):
	ajax = AjaxFollow(request.GET, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

@login_required(login_url='/accounts/login/')
def ajaxsetprofilepic(request):
	ajax = AjaxSetProfilePic(request.POST, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

@login_required(login_url='/accounts/login/')
def ajaxphotofeed(request):
    ajax = AjaxPhotoFeed(request.GET, request.user)
    context = { 'ajax_output': ajax.output() }
    return render(request, 'ajax.html', context)

@login_required(login_url='/accounts/login/')
def ajaxprofilefeed(request):
	ajax = AjaxProfileFeed(request.GET, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)