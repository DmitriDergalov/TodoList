from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
	url(r'^todo/new/$', views.todo_new, name='todo_new'),
	url(r'^todo/(?P<pk>[0-9]+)/del/$', views.todo_del, name='todo_del'),
]
