from django.urls import path
from . import views
from .views import recipe_grid_alt_view

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/about", views.about, name="about"),
    path("recipes-alt/", recipe_grid_alt_view, name="recipe_grid_alt"),
    path("recipe/<int:recipe_id>/", views.recipe_detail, name="recipe_detail"),
]