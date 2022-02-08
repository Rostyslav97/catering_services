from unicodedata import category
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Category, Dish
from .serializers import DishSerializer, DishIDSerializer, DishCategorySerializer

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

class DishRetrieveCategoryAPI(RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishCategorySerializer
    lookup_field = "id"