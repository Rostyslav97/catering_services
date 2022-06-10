from django.contrib import admin
from dish import models


class TabularInlineDish(admin.TabularInline):
    model = models.Dish


class CategorieAdmin(admin.ModelAdmin):
    inlines = [TabularInlineDish]
    list_display = ("name",)


admin.site.register(models.Category, CategorieAdmin)
admin.site.register(models.Dish)
