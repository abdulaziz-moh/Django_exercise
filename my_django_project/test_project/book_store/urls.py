from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("htmlfile/", views.htmlfile,name="htmlfile")
]