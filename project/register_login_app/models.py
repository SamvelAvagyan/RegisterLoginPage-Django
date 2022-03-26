import this
from django.db import models

class User(models.Model):
    name = models.charField(max_length=20)
    surname = models.charField(max_length=25)
    email = models.charField(max_length=35)
    password = models.charFiled(min_length=8)
    confirmPassword = models.charFiled(min_length=8)

    def __str__(self):
        return self.name