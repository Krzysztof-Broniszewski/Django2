from django.contrib import admin
from django.urls import path

from .views import cars_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars_list', cars_list, name='cars_list'),
    # path('kontakt', kontakt, name='kontakt'),
    # path('formularz', create_form_view, name='formularz'),
    # path('opis', opis_widok, name='opis'),
    # path('o_nas', o_nas, name='o Nas'),
]