from django.contrib import admin
from dish import models


class TabularInlineLike(admin.TabularInline):
    model=models.Dish

class CategorieAdmin(admin.ModelAdmin):
    inlines=[TabularInlineLike]
    list_display = ("name",)

admin.site.register(models.Category, CategorieAdmin)

