from django.urls import path
from .api import DishListAPI, DishRetrieveAPI, DishRetrieveIDAPI

app_name = "dishes"

urlpatterns = [
    path("dishes/", DishListAPI.as_view(), name="list"),
    path("dishes/<int:id>/", DishRetrieveAPI.as_view(), name="retrieve"),
    path("dishes/id/<int:id>/", DishRetrieveIDAPI.as_view(), name="retrieve_id"),
    # path("dishes/category/<int:id>/", DishRetrieveCategoryAPI.as_view(), name="retrieve_category"),
    # path("orders/", OrderListCreateSerializerAPI.as_view(), name="orders"),
    # path("orders/<int:id>/", OrderRetrieveAPI.as_view(), name="retrieve_orders")
]