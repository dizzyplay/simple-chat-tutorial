from django.urls import path, re_path
from . import views

app_name = 'chatapp'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<room_name>\w+)/$', views.room, name='room'),
]
