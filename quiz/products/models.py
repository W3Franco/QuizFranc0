from django.contrib.auth.models import User
from django.db import models
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField(default=0)
    numReviews = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
