from ast import Str
from distutils.command.upload import upload
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from .tshirt import Tshirt

class SizeVariant(models.Model):
    SIZES = (
        ('S', "SMALL"),
        ('M', "MEDIUM"),
        ('L', "LARGE"),
        ('XL', "EXTRA LARGE"),
        ('XXL', "EXTRA EXTRA LARGE")
    )
    price = models.IntegerField(null=False)
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    size = models.CharField(choices=SIZES, max_length=5)

    def __str__(self):
        return f'{self.size}'