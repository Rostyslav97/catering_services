from rest_framework import serializers

from .models import Category, Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        exclude = ("id","category")

class DishIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        exclude = ("category",)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"