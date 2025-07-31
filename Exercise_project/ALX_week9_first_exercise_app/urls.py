from django.urls import path,re_path
from . import views

urlpatterns = [
    path("",views.display_homepage),
    path("display_products/",views.product_List),
    re_path(r'^product_detail/(?P<pk>\d+)/$' ,views.product_detail.as_view()),
    # or i can do it using path like this: 
    # path("product_detail/<int:pk>/", views.product_detail.as_view(), name="product_detail"),
    # path("product_detail/", views.product_detail),

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