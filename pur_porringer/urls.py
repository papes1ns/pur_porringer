from django.conf.urls import include, url
from django.contrib import admin

from main.views import ip_broker, index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ip/$', ip_broker, name="ip_broker"),
    url(r'^$', index, name="index"),
]
