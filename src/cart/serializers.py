from rest_framework import serializers
from .models import Cart
from dish.serializers import DishSerializer


class CartSerializer(serializers.ModelSerializer):
    dish = DishSerializer(read_only=True, many=True) 
    class Meta:
        model = Cart
        fields = "__all__"


class CartCreateSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cart
        exclude = ("id", )
