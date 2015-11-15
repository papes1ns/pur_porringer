import datetime
import socket

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

from .models import ip

def index(request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip_address = None
    for obj in ip.objects.filter(active=True):
        try:
            s.connect((obj.ip, 8888))
            ip_address = obj.ip
            s.send("TEST")
        except Exception, e:
            obj.active = False
            obj.save()
    s.close()
    return render(request, "index.html", { "ip": ip_address })

@csrf_exempt
def ip_broker(request):
    ip_address = request.POST.get("ip", None)

    if ip is not None:
        obj, created = ip.objects.get_or_create(ip=ip_address)
        obj.active = True
        obj.modified = datetime.datetime.now()
        obj.save()

    return HttpResponse("GOOD")
