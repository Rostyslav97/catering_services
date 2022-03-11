from rest_framework import serializers

from .models import Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        exclude = ("category",)
        
# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = "__all__"