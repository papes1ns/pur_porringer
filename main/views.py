import datetime
import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

from .models import Command

@csrf_exempt
def index(request):
    if request.method == "POST":
        Command.objects.create()
    cmds = Command.objects.filter(ran=False)
    return render(request, "index.html", { "cmds": cmds })

@csrf_exempt
def command_queue(request):
    try:
        cmd = Command.objects.filter(ran=False)[0]
        cmd.ran = True
        cmd.save()
        return HttpResponse("1")
    except Exception, e:
        print e
        return HttpResponse("0")
