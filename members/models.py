from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dato = models.CharField(max_length=255, default="dato")
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)