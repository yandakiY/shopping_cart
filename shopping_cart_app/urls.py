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
    # details product
    path('<int:prod_id>/details_product' , views.DetailsProduct , name="details_product"),
    # search product by category
    path('search_by' , views.SearchByCategory , name="search_by"),
    # settings 
    path('settings' , views.SettingsViews , name="settings"),
    # setting category
    path('settings_categories' , views.SettingsCategoriesViews , name="settings_categories"),
    # Delete a category
    path('<int:cat_id>/delete_category' , views.DeleteCategory , name="delete_category"),
    path('<int:cat_id>/remove_category' , views.RemoveCategory , name="remove_category"),
    path('<int:cat_id>/update_category' , views.UpdateCategory , name="update_category"),
    path('<int:cat_id>/save_update_category' , views.SaveUpdateCategory , name="save_update_category"),
    # settings product
    path('settings_products' , views.SettingsProductsViews , name="settings_products"),
    # Delete a category
    path('<int:prod_id>/delete_product' , views.DeleteProduct , name="delete_product"),
    path('<int:prod_id>/remove_product' , views.RemoveProduct , name="remove_product"),
    path('<int:prod_id>/update_product' , views.UpdateProduct , name="update_product"),
    path('<int:prod_id>/save_update_product' , views.SaveUpdateProduct , name="save_update_product"),
    # products in corbeille
    path('products_corbeille' , views.ProductsCorbeilleViews , name="products_corbeille"),
    # restore product in corbeille
    path('<int:prod_id>/restore_product' , views.RestoreProduct , name="restore_product")
    
]
