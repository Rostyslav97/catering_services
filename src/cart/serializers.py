from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cart
        fields = "__all__"

class CartDetailSerializer(serializers.ModelSerializer):
    dish = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Cart
        fields = "__all__"
