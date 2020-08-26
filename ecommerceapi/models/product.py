from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .customer import Customer
from .product_type import ProductType

class Product(models.Model):

    title = models.CharField(max_length=55)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    location = models.CharField(max_length=75)
    imagePath = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return self.title