from django.contrib import admin
from cart import models

# class TabularInlineLike(admin.TabularInline):
#     model=models.CartDish

# class CartAdmin(admin.ModelAdmin):
#     inlines=[TabularInlineLike]
#     list_display = ("customer",)

# admin.site.register(models.Cart, CartAdmin)

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
	pass


@admin.register(models.Basket)
class BasketAdmin(admin.ModelAdmin):
	pass
