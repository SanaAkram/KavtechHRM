from django.db import models

# Create your models here.


class User(models.Model):
    # first_name = models.CharField(max_length=10)
    # last_name = models.CharField(max_length=10)
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
