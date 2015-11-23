from datetime import datetime
from paramiko import SSHClient, AutoAddPolicy

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Log

DATETIME_FORMAT = "[ %-I:%M %p ] %A -- %d %B %Y"

def index(request):
    return render(request, "index.html", {
        # 10 latest log enries
        "log": [datetime.strftime(row.ran, DATETIME_FORMAT)
                for row in Log.objects.all().order_by("-ran")[:10]],
    })

def get_connection_ip(request):
    response = call_command("hostname -I")
    if response is None:
        return HttpResponse(None)
    return HttpResponse(response)

def call_motor_and_log(request):
    response = call_command("sudo ./motor_on.py")
    if response is None:
        return HttpResponse("Unable to dispense food", None, 403)
    row = Log.objects.create()
    return HttpResponse(datetime.strftime(row.ran, DATETIME_FORMAT))

def call_command(cmd):
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        client.connect("127.0.0.1", 2222, "pi", "raspberry")
    except Exception, e:
        return None
    stdin, stdout, stderr = client.exec_command(cmd)
    return stdout.read()
