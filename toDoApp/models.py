from django.db import models
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()

class ToDo(models.Model):
    
    item = models.CharField(max_length=500)
    user = models.ForeignKey(UserModel, on_delete= models.CASCADE, related_name="todos")

    class Meta: 
        verbose_name_plural = 'todos'
