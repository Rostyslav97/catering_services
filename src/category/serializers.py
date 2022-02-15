from rest_framework import serializers
from core.models import Dish


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("name", "category")