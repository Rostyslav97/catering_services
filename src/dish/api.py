from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveAPIView
from .models import Dish
from .serializers import DishSerializer


class DishListAPI(ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishRetrieveAPI(RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    lookup_field = "id"

