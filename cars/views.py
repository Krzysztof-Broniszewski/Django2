from django.shortcuts import render
from .models import Car
# from django.http import HttpResponse


# Create your views here.

def cars_list(request):
    cars = Car.objects.all().order_by('car')
    return render(request, "cars_list.html", {'cars': cars} )
