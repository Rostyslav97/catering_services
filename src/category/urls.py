from django.urls import path
from .api import CategoryRetrieveAPI

app_name = "category"

urlpatterns = [path("categories/<int:id>/", CategoryRetrieveAPI.as_view(), name="retrieve")]
