from rest_framework import serializers
from .models import Order, Basket
from dish.serializers import DishSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions",
            "date_joined",
        )


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = "__all__"


class BasketSeralizer(serializers.ModelSerializer):
    dish = DishSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = "__all__"


class BaskerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
