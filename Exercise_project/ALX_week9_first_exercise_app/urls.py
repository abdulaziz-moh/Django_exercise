from django.urls import path
from . import views

urlpatterns = [
    path("",views.display_homepage),
    path("display_products/",views.product_List),
    path("product_detail/",views.product_detail),
    path("create_product/",views.create_product),
    path("update/",views.update_product),
    path("delete/",views.delete_product),
    
    
    path("add_product_discription/",views.add_product_discription),
    path("functionwith_prefetch_related/",views.functionwith_prefetch_related),
    path("create_student/",views.create_student),
    path("create_cource/",views.create_cource),
    path("enrlol_student/",views.enrlol_student),
    path("display_stu_crc/",views.display_stu_crc.as_view()),
    
]