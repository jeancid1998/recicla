# chat/urls.py
from django.conf.urls import url
from django.urls import re_path

from .views import indexchat, room

app_name = "chat";
urlpatterns = [
    url(r'^$', indexchat, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]