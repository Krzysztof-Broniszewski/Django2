from django.contrib import admin

from .models import Car

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ['car', 'engine', 'gear_box', 'doors']
    list_display = ['car', 'model']
    search_fields = ['car']
