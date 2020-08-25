from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .customer import Customer
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
        verbose_name = ("producttype")
        verbose_name_plural = ("producttypes")

    def __str__(self):
        return self.name

 Id int PK
  Title varchar(50)
  CustomerId int
  Price decimal
  Description varchar(255)
  Quantity int
  Location varchar(75)
  ImagePath varchar(255)
  CreatedAt datetime
  ProductTypeId int