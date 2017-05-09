from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproj.views.home', name='home'),
	
    url(r'', include('todolist.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
