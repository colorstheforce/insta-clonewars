from django.conf.urls import url
from . import views

app_name = 'userprofile'

urlpatterns = [

    url(r'^follow_toggle/$', views.follow_toggle, name='follow_toggle'),
    url(r'^edit-info/', views.edit_info, name='edit_info'),
    url(r'^search/', views.search, name='searchuser'),
    url(r'^(?P<username>\w+)/followers/$', views.followers, name='followers'),
    url(r'^(?P<username>\w+)/following/$', views.following, name='following'),
    
    url(r'^(?P<user_username>\w+)/$', views.profile, name='see_user'),

    url(r'^profile$', views.profile, name="profile"),

    url(r'^ajax-set-profile-pic$', views.ajaxsetprofilepic),
    url(r'^ajax-profile-feed$', views.ajaxprofilefeed),
  
    url(r'^ajax-follow$', views.ajaxfollow),
  
    url(r'^ajax-photo-feed$', views.ajaxphotofeed),

]