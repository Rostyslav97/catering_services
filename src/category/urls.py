from django.urls import path
from .api import CategoryRetrieveAPI

app_name = "category"

urlpatterns = [
    path("category/<int:id>/", CategoryRetrieveAPI.as_view(), name="category")
]
