from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30)
    year = models.IntegerField()
    color = models.CharField(max_length=12)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()