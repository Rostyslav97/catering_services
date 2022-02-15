from rest_framework.generics import RetrieveAPIView
from core.models import Dish
from .serializers import CategorySerializer

class CategoryRetrieveAPI(RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"