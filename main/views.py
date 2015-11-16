import datetime
from paramiko import SSHClient, AutoAddPolicy

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

from .models import Command

@csrf_exempt
def index(request):
    if request.method == "POST":
        call_motor_on()
    return render(request, "index.html")


def call_motor_on():
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect("127.0.0.1", 2222, "pi", "raspberry")
    stdin, stdout, stderr = client.exec_command("ls ~/Desktop")

    for line in stdout.read().splitlines():
        print line
