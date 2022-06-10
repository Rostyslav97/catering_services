from django.urls import path
from .api import DishListAPI, DishRetrieveAPI

app_name = "dishes"

urlpatterns = [
    path("dishes/", DishListAPI.as_view(), name="list"),
    path("dishes/<int:id>/", DishRetrieveAPI.as_view(), name="retrieve"),
]
