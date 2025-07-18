from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)
    category = models.CharField(max_length=100)
    id = models.IntegerField(unique=True, ord = True)

    def __init__(self):
        return self.name