from urllib.request import BaseHandler
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # 
    return render(request, "dom.html", {})

def kontakt(request, *args, **kwargs):
    # return HttpResponse("<h1>Kontakt do mnie</h1>")
    return render(request, "kontakt.html", {})

def o_nas(request, *args, **kwargs):
    # return HttpResponse("<h1>Kilka słów o nas</h1>")
    return render(request, "onas.html", {})
