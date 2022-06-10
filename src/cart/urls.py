from django.urls import path
from .api import (
    OrderListAPI,
    OrderRetrieveAPI,
    OrderCreateAPI,
    BasketRetrieveAPI,
    BasketCreateAPI,
)

app_name = "cart"

urlpatterns = [
    path("orders/", OrderListAPI.as_view(), name="list"),
    path("orders/<int:id>/", OrderRetrieveAPI.as_view(), name="retrieve"),
    path("orders/create/", OrderCreateAPI.as_view(), name="create"),
    path("baskets/<int:id>/", BasketRetrieveAPI.as_view(), name="retrieve"),
    path("baskets/create/", BasketCreateAPI.as_view(), name="create"),
]
