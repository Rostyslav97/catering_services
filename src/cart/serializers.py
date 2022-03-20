from rest_framework import serializers
from .models import Cart, CartDish

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"