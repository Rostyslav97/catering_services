from rest_framework import serializers
from .models import Cart, CartDish

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDish
        fields = "__all__"