from django.db import models
from django.conf import settings


class Dish(models.Model):
    name = models.CharField(max_length=70, unique=True)
    description = models.TextField()
    spicy = models.BooleanField(null=True, blank=True, default=None)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    output = models.CharField(max_length=20)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Category(models.Model):
    name = models.TextField()

class Order(models.Model):
    dish = models.ForeignKey("Dish", on_delete=models.CASCADE)
    amount = models.CharField(max_length=200)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL)
    delivery_date = models.DateTimeField()