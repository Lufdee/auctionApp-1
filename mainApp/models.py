from django.db import models
from datetime import date
import random

class User(models.Model):
    username = models.EmailField(max_length=40)
    password = models.CharField(max_length=40)
    id = models.IntegerField(primary_key=True)

    """ Returns object name """
    def __str__(self):
        return self.username

    """ Converts the variables to dictionary """
    def to_dict(self):
        return {
            'id' : self.id,
            'username': self.username,
            'password': self.password,
        }
    