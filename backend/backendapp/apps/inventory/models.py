import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import constants


class Supplier(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    note = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="inventories"
    )

    class Meta:
        verbose_name = "inventory"
        verbose_name_plural = "inventories"

    def __str__(self):
        return self.name
