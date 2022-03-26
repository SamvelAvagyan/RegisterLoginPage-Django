import this
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    password = models.CharField(max_length=50)
    confirmPassword = models.CharField(max_length=50)

    def __str__(self):
        return self.name