from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    occupation = models.CharField(max_length=50)
