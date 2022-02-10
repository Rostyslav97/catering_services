from rest_framework import serializers

from .models import Dish, Order

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        exclude = ("id","category")

class DishIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        exclude = ("category",)

class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("name", "category")

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"