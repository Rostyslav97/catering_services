from django.urls import path
from .api import DishListAPI, DishRetrieveAPI, DishRetrieveIDAPI, DishRetrieveCategoryAPI

app_name = "dishes"

urlpatterns = [
    path("", DishListAPI.as_view(), name="list"),
    path ("<int:id>/", DishRetrieveAPI.as_view(), name="retrieve"),
    path("id/<int:id>/", DishRetrieveIDAPI.as_view(), name="retrieve_id"),
    path("category/<int:id>/", DishRetrieveCategoryAPI.as_view(), name="retrieve_category")
]