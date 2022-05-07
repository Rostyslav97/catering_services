from django.urls import path
from .api import CartListAPI, CartRetrieveAPI, CartCreateAPI

app_name = "cart"

urlpatterns = [
    path("cart/", CartListAPI.as_view(), name="cart"),
    path("cart/<int:id>/", CartRetrieveAPI.as_view(), name="cart_retrieve"),
    path("cart/create/", CartCreateAPI.as_view(), name="cart_create"),
]
