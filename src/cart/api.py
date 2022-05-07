from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Cart
from .serializers import CartSerializer, CartCreateSerializer
from .permissions import IsAdmin, IsOwner, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CartListAPI(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CartRetrieveAPI(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "id"
    permission_classes = (IsAdmin, )


class CartCreateAPI(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer
    permission_classes = (IsAuthenticated, )
