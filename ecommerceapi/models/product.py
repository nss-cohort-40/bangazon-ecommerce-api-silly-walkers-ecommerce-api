from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .
from .product_type import ProductType

class Product(models.Model):

    name = models.CharField(max_length=55)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    price = models.DecimalField
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    location = models.CharField(max_length=75)
    imagePath = models.CharField(max_length=255)
    createdAt = models.DateTimeField()
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return self.name