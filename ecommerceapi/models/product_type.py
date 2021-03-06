from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProductType(models.Model):

    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = ("producttype")
        verbose_name_plural = ("producttypes")

    def __str__(self):
        return self.name
