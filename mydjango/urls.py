"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from strony.views import home_view, kontakt, o_nas

from Produkty.views import create_form_view, opis_widok

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('kontakt', kontakt, name='kontakt'),
    path('formularz', create_form_view, name='formularz'),
    path('opis', opis_widok, name='opis'),
    path('o_nas', o_nas, name='o Nas'),
]
