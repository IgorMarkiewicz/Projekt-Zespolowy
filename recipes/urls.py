from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/about", views.about, name="about"),
]