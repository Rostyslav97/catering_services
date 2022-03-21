from django.db import models
from django.conf import settings
from dish.models import Dish

class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL)
    delivery_date = models.DateTimeField()
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    amount = models.IntegerField() 