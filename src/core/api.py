from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveAPIView
from .models import Dish
from .serializers import DishSerializer, DishIDSerializer

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

# class OrderListCreateSerializerAPI(ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class OrderRetrieveAPI(RetrieveAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     lookup_field = "id"