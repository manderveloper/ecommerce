from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=150)
    description = models.TextField('Description')
    price       = models.DecimalField(max_digits=7, decimal_places=2)

    def get_absolute_url(self):
        return reverse("", kwargs={"id": self.id})

