from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from recipes.models import Recipe

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def recipe_grid_alt_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_grid_alt.html', {'recipes': recipes})

def about(request):
    return render(request, 'about.html')

def recipe_detail(request, recipe_id,):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
def account_recipes(request, user_id,):
    user = get_object_or_404(User, pk=user_id)
    recipes_id = Recipe.objects.filter(user=user)
    return render(request, 'account_recipes.html', {'recipes': recipes_id, 'user': user})