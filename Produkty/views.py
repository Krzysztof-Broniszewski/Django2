from django.shortcuts import render

from .models import Produkt
from .forms import ProduktForm

# Create your views here.

def create_form_view(request):
    form = ProduktForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = ProduktForm()

    kontekst = {
        'form' : form
    }

    return render (request, "products/create_product.html", kontekst)

def opis_widok(request):
    obj = Produkt.objects.get(id=2)

    kontekst = {
        'object' : obj
    }

    return render (request, "products/opis.html", kontekst)