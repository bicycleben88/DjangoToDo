from tabnanny import verbose
from django.db import models

class Dog(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta: 
        verbose_name_plural = 'dogs'

class ToDo(models.Model):
    
    item = models.CharField(max_length=500)

    class Meta: 
        verbose_name_plural = 'todos'