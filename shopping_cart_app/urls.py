from . import views
from django.urls import path

app_name="shopCart"

urlpatterns = [
    path('' , views.Index , name="Index"),
    # create category
    path('create_category', views.AddCategory.as_view() , name="create_category"),
    path('save_create_category', views.SaveCategory , name="save_create_category"),
    # create a product
    path('create_product' , views.AddProduct , name="create_product"),
    path('save_create_product' , views.SaveProduct , name="save_create_product"),
]
