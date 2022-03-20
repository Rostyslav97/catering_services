from django.db import models
from django.conf import settings

class CartDish(models.Model):
    amount = models.IntegerField() 

class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL)
    delivery_date = models.DateTimeField()
    dish = models.ManyToManyField(CartDish, related_name = 'dish')