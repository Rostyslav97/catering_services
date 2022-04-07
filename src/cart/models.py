from django.db import models
from django.conf import settings
from dish.models import Dish

class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL)
    delivery_date = models.DateTimeField(auto_now_add=True)
    dish = models.ManyToManyField(Dish)
    amount = models.IntegerField() 
