from rest_framework import serializers

from .models import Dish

class DishSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Dish
        exclude = ("id",)
        
# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = "__all__"