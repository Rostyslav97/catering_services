from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from .models import Cart
from .serializers import CartSerializer, CartDetailSerializer
from rest_framework.permissions import IsAuthenticated


class CartListCreateAPI(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartRetrieveAPI(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer
    lookup_field = "id"
    permission_classes = (IsAuthenticated, )