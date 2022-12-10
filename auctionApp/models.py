from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import date
import random

class CustomUser(AbstractBaseUser):

#resource used to construct model: https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project

    userPassword = models.CharField(max_length=40)
    userName = models.CharField(max_length=40, unique = True, primary_key=True)
    userEmail = models.EmailField(max_length = 254, unique = True)
    userDateOfBirth = models.DateField(max_length=8)

    #images in a model: https://stackoverflow.com/questions/6396442/add-image-avatar-field-to-users
    userImage = models.ImageField(upload_to='images')

    USERNAME_FIELD = 'userEmail'
    REQUIRED_FIELDS = ['userEmail', 'userName' 'userDateOfBirth', 'userImage']


    """ Returns object name """
    def __str__(self):
        return self.userName

    """ Converts the variables to dictionary """
    def to_dict(self):
        return {
            'id' : self.id,
            'username': self.userName,
            'password': self.userPassword,
            'email' : self.userEmail,

        }
    #orders db entries by email address and names the table User
    class Meta:
        ordering = ["userEmail"]
        verbose_name = "User"