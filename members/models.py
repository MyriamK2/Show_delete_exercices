from django.db import models

# Create your models here.
class Member(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    name = models.CharField(max_length=30)
    age = models.PositiveBigIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)