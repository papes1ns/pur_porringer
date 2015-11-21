import datetime
from paramiko import SSHClient, AutoAddPolicy

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Log

@csrf_exempt
def index(request):
    context = {}
    client = is_connected()
    if request.method == "POST" and client != False:
        try:
            call_motor_on(client)
            Log.objects.create()
            return HttpResponseRedirect(reverse("index"))
        except Exception, e:
            print e

    context["client"] = client
    context["log"] = Log.objects.all().order_by("-ran")[:10]
    return render(request, "index.html", context)


def call_motor_on(client):
    stdin, stdout, stderr = client.exec_command("sudo ./motor_on.py")

def is_connected():
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        client.connect("127.0.0.1", 2222, "pi", "raspberry")
        return client
    except Exception, e:
        print e
        return False
