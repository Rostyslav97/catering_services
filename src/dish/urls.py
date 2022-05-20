from django.urls import path
from .api import DishListAPI, DishRetrieveAPI

app_name = "dishes"

urlpatterns = [
    path("dish/", DishListAPI.as_view(), name="list"),
    path("dish/<int:id>/", DishRetrieveAPI.as_view(), name="retrieve"),
]
