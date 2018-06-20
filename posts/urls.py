from django.conf.urls import url, include
from  . import views

urlpatterns = [

    url(r'^home$', views.home,name="home"),
    # url(r'^ajax-profile-feed$', views.ajaxprofilefeed),
    url(r'^image/(?P<pid>\d+)$',views.image, name="image"),
    url(r'^ajax-image$', views.ajaximage),
    url(r'^ajax-save-photo$', views.ajaxsavephoto),
    url(r'^ajax-like-photo$', views.ajaxlikephoto),
    url(r'^ajax-tag$', views.ajaxtag),
    url(r'^ajax-photo-feed$', views.ajaxphotofeed),
    # re_path(r'^image/ajax-image$', views.ajaximage),
    # path('image/<int:pid>',views.image, name="image")
]