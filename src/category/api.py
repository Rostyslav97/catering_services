from rest_framework.generics import RetrieveAPIView
from dish.models import Category
from category.serializers import CategorySerializer


class CategoryRetrieveAPI(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"
