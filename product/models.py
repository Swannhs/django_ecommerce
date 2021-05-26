from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    # image =
    shortDescription = models.TextField(null=True, blank=True)
    fullDescription = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    rating = models.DateTimeField(max_digits=7, decimal_places=2, null=True, blank=True, default=0)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DateTimeField(max_degits=7, decimal_places=2, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    id = models.AutoField(primary_key=True, editable=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)
