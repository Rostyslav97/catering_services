from django.contrib import admin
from cart import models

# class TabularInlineLike(admin.TabularInline):
#     model=models.Cart_dish

# class CartAdmin(admin.ModelAdmin):
#     inlines=[TabularInlineLike]
#     list_display = ("customer",)

# admin.site.register(models.Cart, CartAdmin)