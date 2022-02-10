from django.contrib import admin
from core import models
# from .models import Dish, Category

class TabularInlineLike(admin.TabularInline):
    model=models.Dish

class CategorieAdmin(admin.ModelAdmin):
    inlines=[TabularInlineLike]
    list_display = ("name",)

admin.site.register(models.Category, CategorieAdmin)

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
	pass


# @admin.register(Dish)
# class DishAdmin(admin.ModelAdmin):
# 	pass

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
# 	pass
