from urllib.request import BaseHandler
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # 
    return render(request, "dom.html", {})

def kontakt(request, *args, **kwargs):
    kontekst = {
        "users" : ["user1", "user2", "user3", "user4"],
        "phone_number" : 1123,
        "numbers" : [123, 456, 789, 123]
    }

    # return HttpResponse("<h1>Kontakt do mnie</h1>")
    return render(request, "kontakt.html", kontekst)

def o_nas(request, *args, **kwargs):
    # return HttpResponse("<h1>Kilka słów o nas</h1>")
    return render(request, "onas.html", {})
