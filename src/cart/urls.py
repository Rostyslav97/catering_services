from django.urls import path
from .api import OrderListAPI, OrderRetrieveAPI, OrderCreateAPI, BasketRetrieveAPI, BasketCreateAPI

app_name = "cart"

urlpatterns = [
    path("order/", OrderListAPI.as_view(), name="order"),
    path("order/<int:id>/", OrderRetrieveAPI.as_view(), name="order_retrieve"),
    path("order/create/", OrderCreateAPI.as_view(), name="order_create"),
    path('basket/<int:id>/', BasketRetrieveAPI.as_view(), name="basket_retrieve"),
    path('basket/create/', BasketCreateAPI.as_view(), name='basket_create')
]
