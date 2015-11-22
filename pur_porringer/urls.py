from django.conf.urls import include, url
from django.contrib import admin

from main.views import index, get_connection_ip, call_motor_and_log

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name="index"),
    url(r'^get_connection_ip/$', get_connection_ip, name="get_connection_ip"),
    url(r'^call_motor_and_log/$', call_motor_and_log, name="call_motor_and_log"),
]
