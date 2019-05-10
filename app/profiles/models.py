from django.db import models

# Create your models here.
class Profiles(models.Model):
    user        = models.CharField(max_length=150)
    email       = models.EmailField('Email Address')
    password    = models.CharField(max_length=100)





