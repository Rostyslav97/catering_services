from unicodedata import category
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Category, Dish
from .serializers import DishSerializer, DishIDSerializer, CategorySerializer

class DishListAPI(ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishRetrieveAPI(RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    lookup_field = "id"

class DishRetrieveIDAPI(RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishIDSerializer
    lookup_field = "id"

class CategoryRetrieveAPI(RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"