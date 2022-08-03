from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=500, null=True)


class KavProf(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    usertype = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    experience = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "account_kavprof"
