from django.db import models
from django.conf import settings

class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL)
    delivery_date = models.DateTimeField()

class Cart_dish(models.Model):
    dish = models.ManyToManyField(Cart)
    amount = models.IntegerField()