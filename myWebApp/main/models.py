from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=200)
    productDescription = models.TextField()
    productCost = models.IntegerField()
    datePublished = models.DateTimeField("date published", default=datetime.now)

    def __str__(self):
        return self.productName

