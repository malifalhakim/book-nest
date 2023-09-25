from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    amount = models.IntegerField()
    author = models.CharField(max_length=255)
    description = models.TextField()