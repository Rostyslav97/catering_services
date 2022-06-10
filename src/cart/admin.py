from django.contrib import admin
from cart import models


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Basket)
class BasketAdmin(admin.ModelAdmin):
    pass
