from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.first_name + self.username

class Customer(models.Model):
    profile_number = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.profile_number) + " " + str(self.user)