from django.urls import path
from . import views
from .views import allergen_list
from .views import user_list

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/about", views.about, name="about"),
    path('allergens/', allergen_list, name='allergen_list'),
    path('users/', user_list, name='user_list'),
]