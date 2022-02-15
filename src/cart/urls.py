from django.urls import path
from .api import CartListCreateAPI, CartRetrieveAPI

app_name = "cart"

urlpatterns = [
    path("cart/", CartListCreateAPI.as_view(), name="cart"),
    path("cart/<int:id>/", CartRetrieveAPI.as_view(), name="cart_retrieve")
]