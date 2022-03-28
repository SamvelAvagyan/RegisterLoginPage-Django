import this
from django.db import models
from django.forms import NullBooleanField

class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    password = models.CharField(max_length=50)
    confirmPassword = models.CharField(max_length=50)
    isVerified = models.BooleanField(default=False)
    auth_token = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name