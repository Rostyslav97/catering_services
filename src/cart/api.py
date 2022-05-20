from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Order, Basket
from .serializers import OrderSerializer, OrderCreateSerializer, BasketSeralizer, BaskerCreateSerializer
from .permissions import IsAdmin, IsOwner, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class OrderListAPI(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdmin, )


class OrderRetrieveAPI(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "id"
    permission_classes = (IsAdmin, )


class OrderCreateAPI(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (IsAuthenticated, )





class BasketRetrieveAPI(RetrieveAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSeralizer
    lookup_field = "id"
    permission_classes = (IsAuthenticated, )


class BasketCreateAPI(CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BaskerCreateSerializer
    permission_classes = (IsAuthenticated, )