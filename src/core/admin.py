from django.contrib import admin
from core import models
# from category.models import Category
# from category import models
# from .models import Dish, Category
# from .models import DishOrder


class TabularInlineLike(admin.TabularInline):
    model=models.Dish

class CategorieAdmin(admin.ModelAdmin):
    inlines=[TabularInlineLike]
    list_display = ("name",)

admin.site.register(models.Category, CategorieAdmin)

# @admin.register(models.Order)
# class OrderAdmin(admin.ModelAdmin):
# 	pass


# @admin.register(models.Dish)
# class DishAdmin(admin.ModelAdmin):
# 	pass

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
# 	pass
