from rest_framework import serializers
from .models import Cart, Cart_dish

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_dish
        fields = "__all__"