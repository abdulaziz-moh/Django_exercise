from django.urls import path
from . import views

urlpatterns = [
    path("",views.display_homepage),
    path("display_products/",views.product_List),
    path("product_detail/",views.product_detail),
    path("create_product/",views.create_product),
    path("update/",views.update_product),
    path("delete/",views.delete_product),
]