from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as authviews

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^logout/$', authviews.logout, {"next_page": '/'}, name="logout"), 
]