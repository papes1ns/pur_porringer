from django.conf.urls import include, url
from django.contrib import admin

from main.views import command_queue, index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^queue/$', command_queue, name="command_queue"),
    url(r'^$', index, name="index"),
]
