from django.db import models

class User(models.Model):
    name      = models.CharField(max_length=40) 
    email     = models.EmailField()
    password  = models.TextField()
