from django.db import models
from django.conf import settings
from dish.models import Dish


class Order(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL
    )

    def __str__(self):
        return str(self.customer)


class Basket(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    amount = models.SmallIntegerField(null=False, blank=False)
    delivery_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.dish)
