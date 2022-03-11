from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Cart, CartDish
from .serializers import CartSerializer

class CartListCreateAPI(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartRetrieveAPI(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "id"