from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from .models import Cart
from .serializers import CartSerializer, CartDetailSerializer
from .permissions import IsAdmin, IsOwner, IsOwnerOrReadOnly


class CartListCreateAPI(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CartRetrieveAPI(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer
    lookup_field = "id"
    permission_classes = (IsAdmin, )