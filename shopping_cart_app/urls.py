from . import views
from django.urls import path

app_name="shopCart"

urlpatterns = [
    path('' , views.Index , name="Index")
]
