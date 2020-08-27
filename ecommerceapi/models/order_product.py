from django.db import models
from .product import Product
from .order import Order


class OrderProduct(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name="cart")
    order = models.ForeignKey(
        Order, on_delete=models.DO_NOTHING, related_name="cart")

    class Meta:
        verbose_name = ("order product")
        verbose_name_plural = ("orders products")
