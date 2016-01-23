# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

import subprocess

def index(request):
    return render_to_response("index.html", {}, context_instance=RequestContext(request))

@csrf_protect
def print_picture(request):
    if request.is_ajax() and request.method == "POST":
        data = request.POST.get("base64Image")
        _, image = data.split('base64,')
        base64img = image.decode('base64')
        
        try:
            p = subprocess.Popen(["lp", "-o", "media=a4", "-o", "scaling=50", "-o", "fitplot"], stdin=subprocess.PIPE)
            p.communicate(base64img)
        except:
            return HttpResponse(status=500)
    return HttpResponse(status=200)