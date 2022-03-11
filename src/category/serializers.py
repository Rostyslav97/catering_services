from rest_framework import serializers
from dish.models import Dish


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("name", "category")