from django.urls import path
from .api import DishListAPI, DishRetrieveAPI

app_name = "dishes"

urlpatterns = [
    path("dish/", DishListAPI.as_view(), name="list"),
    path("dish/<int:id>/", DishRetrieveAPI.as_view(), name="retrieve"),
    # path("dishes/category/<int:id>/", DishRetrieveCategoryAPI.as_view(), name="retrieve_category"),
    # path("orders/", OrderListCreateSerializerAPI.as_view(), name="orders"),
    # path("orders/<int:id>/", OrderRetrieveAPI.as_view(), name="retrieve_orders")
]