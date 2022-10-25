from random import choices
from django.db import models

# Create your models here.

ENGINE = (
    ('diesel', 'Diesel'),
    ('benzin', 'Benzin'),
    ('electric', 'Electric'),
    ('hybrid', 'Hybrid')
)

GEAR_BOX = (
    ('manual', 'manual'),
    ('automatic', 'automatic'),
    ('dsg', 'dsg')
)

class Car(models.Model):
    car = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    engine = models.CharField(choices=ENGINE, max_length=30, default='diesel')
    gear_box = models.CharField(choices=GEAR_BOX, max_length=30, default='manual')
    doors = models.DecimalField(max_digits=1, decimal_places=0, default=5)
    colour = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000)

    def __str__(self):
        return self.car
