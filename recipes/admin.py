from django.contrib import admin

from recipes.models import Recipe, Ingredient, Category, Allergen, Rating

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Allergen)
admin.site.register(Rating)

