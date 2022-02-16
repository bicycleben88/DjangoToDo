from tabnanny import verbose
from django.db import models

class Dog(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta: 
        verbose_name_plural = 'dogs'
